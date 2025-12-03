# Desafio 4: Microsserviços Independentes

Este desafio demonstra a comunicação direta entre dois microsserviços via HTTP em uma rede isolada.

## Serviços

1.  **Service A (Provider):** `BookCatalog`
    *   Tecnologia: Python Flask
    *   Porta: 8081
    *   Função: Serve um JSON com uma lista de livros.

2.  **Service B (Consumer):** `LibraryDisplay`
    *   Tecnologia: Python Flask
    *   Porta: 8082
    *   Função: Consome a API do `BookCatalog` e renderiza uma lista HTML para o usuário final.

## Como Executar

1.  **Criar a Rede:**
    ```bash
    docker network create books_net
    ```

2.  **Build das Imagens:**
    ```bash
    docker build -t book_catalog ./service_a
    docker build -t library_display ./service_b
    ```

3.  **Rodar o Catálogo (Service A):**
    ```bash
    docker run -d --name book_catalog --network books_net -p 8081:8081 book_catalog
    ```

4.  **Rodar o Display (Service B):**
    ```bash
    docker run -d --name library_display --network books_net -p 8082:8082 library_display
    ```

5.  **Acessar:**
    Abra o navegador em `http://localhost:8082`. Você verá a lista de livros formatada.
    Você também pode acessar a API crua em `http://localhost:8081/books`.
