from flask import Flask
import requests

app = Flask(__name__)

CATALOG_SERVICE_URL = "http://book_catalog:8081/books"

@app.route('/')
def index():
    try:
        response = requests.get(CATALOG_SERVICE_URL)
        response.raise_for_status()
        books = response.json()
        
        html = "<h1>Biblioteca (LibraryDisplay)</h1><ul>"
        for book in books:
            html += f"<li><b>{book['title']}</b> por <i>{book['author']}</i></li>"
        html += "</ul>"
        return html
    except Exception as e:
        return f"<h1>Erro ao conectar com o Catálogo de Livros</h1><p>{e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
