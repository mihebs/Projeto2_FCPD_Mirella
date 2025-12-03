import time
import os
from datetime import datetime

FILE_PATH = "/var/data/storage/app_data.txt"

def main():
    print(f"Iniciando Logger Simples. Arquivo alvo: {FILE_PATH}")
    
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Registro de log automático: {timestamp}\n"
        
        try:
            with open(FILE_PATH, "a") as f:
                f.write(log_entry)
            print(f"Dados persistidos: {log_entry.strip()}")
        except IOError as e:
            print(f"Erro crítico de I/O: {e}")
            
        time.sleep(3)

if __name__ == "__main__":
    main()

