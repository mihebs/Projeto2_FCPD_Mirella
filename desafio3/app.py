from flask import Flask
import pymysql
from pymemcache.client import base
import time
import os

app = Flask(__name__)

# Configurações (Variáveis de Ambiente ou Defaults)
DB_HOST = os.getenv('DB_HOST', 'sql_db')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'secret')
DB_NAME = os.getenv('DB_NAME', 'testdb')

CACHE_HOST = os.getenv('CACHE_HOST', 'cache_service')
CACHE_PORT = 11211

def get_db_connection():
    return pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           database=DB_NAME,
                           cursorclass=pymysql.cursors.DictCursor)

def get_memcached_client():
    return base.Client((CACHE_HOST, CACHE_PORT))

def init_db():
    """Inicializa a tabela se não existir."""
    # Wait loop simples para o MySQL subir
    retries = 5
    while retries > 0:
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, count INT)")
                cursor.execute("INSERT INTO visits (count) SELECT 0 WHERE NOT EXISTS (SELECT * FROM visits)")
                conn.commit()
            conn.close()
            print("Database connected and initialized.")
            return
        except pymysql.MySQLError as e:
            print(f"Waiting for DB... {e}")
            time.sleep(5)
            retries -= 1

@app.route('/')
def index():
    client = get_memcached_client()
    
    # Tenta pegar do Cache (Memcached)
    count = client.get('visit_count')
    
    if count is None:
        print("Cache MISS. Fetching from MySQL.")
        # Se não está no cache, pega do DB
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT count FROM visits LIMIT 1")
            result = cursor.fetchone()
            count = result['count'] + 1
            
            # Atualiza DB
            cursor.execute("UPDATE visits SET count = %s", (count,))
            conn.commit()
        conn.close()
        
        # Atualiza Cache
        client.set('visit_count', str(count), expire=10) # Expira em 10s para teste
    else:
        print("Cache HIT.")
        count = int(count) + 1
        # Em um cenário real, escreveríamos no DB eventualmente (write-back), 
        # mas aqui vamos apenas incrementar no cache para demonstrar o hit.
        # Para consistência total no desafio, vamos atualizar ambos, mas marcando a origem.
        
        # Update DB to keep sync simple for this demo
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE visits SET count = %s", (count,))
            conn.commit()
        conn.close()
        client.set('visit_count', str(count), expire=10)

    return f"<h1>Desafio 3: Orchestration</h1><p>Visitas: {count}</p><p>Backend: Flask + MySQL + Memcached</p>"

if __name__ == "__main__":
    time.sleep(10) # Aguarda serviços subirem (pobre man's wait-for-it)
    init_db()
    app.run(host='0.0.0.0', port=5000)
