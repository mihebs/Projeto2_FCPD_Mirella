# Desafio 2: Volumes e Persistência de Dados

Este desafio foca na persistência de dados utilizando Volumes do Docker. O objetivo é garantir que os dados gerados pela aplicação sobrevivam à destruição do container.

## Estrutura do Desafio

*   **Aplicação:** Um script Python ("Log Storage") que escreve a data e hora atual em um arquivo de texto a cada 3 segundos.
*   **Caminho do Arquivo:** `/var/data/storage/app_data.txt`

## Mecanismo de Persistência

O script Python foi configurado para escrever em um caminho absoluto específico. Para que esses dados persistam, este diretório dentro do container deve ser mapeado para um Volume Docker ou um diretório no host (Bind Mount) durante a execução.

## Como Executar e Testar

1.  **Build da Imagem:**
    ```bash
    docker build -t desafio2-app .
    ```

2.  **Criar o Volume:**
    ```bash
    docker volume create dados_persistentes
    ```

3.  **Rodar o Container (com Volume):**
    ```bash
    docker run -d --name app_persistencia -v dados_persistentes:/var/data/storage desafio2-app
    ```

4.  **Verificar os Logs (Escrita):**
    ```bash
    docker logs -f app_persistencia
    ```

5.  **Prova de Persistência:**
    *   Pare e remova o container: `docker rm -f app_persistencia`
    *   Inicie um novo container com o **mesmo volume**:
        ```bash
        docker run -d --name app_persistencia_v2 -v dados_persistentes:/var/data/storage desafio2-app
        ```
    *   Verifique o conteúdo do arquivo. Você verá os logs antigos seguidos pelos novos.
        ```bash
        docker exec -it app_persistencia_v2 cat /var/data/storage/app_data.txt
        ```
