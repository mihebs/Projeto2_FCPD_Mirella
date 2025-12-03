# Desafio 3: Orquestração com Docker Compose

Este desafio orquestra uma aplicação web com banco de dados e cache utilizando o Docker Compose.

## Stack Tecnológica (The "LAMP/Legacy" Approach)

*   **Web Frontend:** Python Flask.
*   **Banco de Dados:** MySQL (em vez de Postgres).
*   **Cache:** Memcached (em vez de Redis).
*   **Rede:** `internal_compose_net`.

## Decisão Técnica: Memcached vs Redis

Para este desafio, optamos explicitamente pelo **Memcached**.

1.  **Simplicidade e Multithreading:** O Memcached é historicamente conhecido pela sua arquitetura multithreaded simples e extremamente performática para armazenamento chave-valor puro (cache de objetos).
2.  **Foco Específico:** Diferente do Redis, que é um "Data Structure Store" (com suporte a listas, sets, persistência, pub/sub), o Memcached foca apenas em ser um cache LRU (Least Recently Used) volátil e rápido.
3.  **Cenário "Legacy":** Em muitas arquiteturas legadas ou específicas de alta performance simples (como cache de sessões ou queries SQL puras), o Memcached ainda é uma escolha robusta e amplamente encontrada. Ele consome menos memória overhead para chaves pequenas em alguns cenários.

## Como Executar

1.  **Subir a Stack:**
    ```bash
    docker-compose up --build
    ```

2.  **Acessar a Aplicação:**
    Abra o navegador ou use curl em `http://localhost:5000`.
    Você verá o contador de visitas sendo incrementado.

3.  **Testar Cache:**
    Observe os logs (`docker-compose logs -f web_frontend`).
    A primeira requisição buscará no MySQL ("Cache MISS").
    Requisições subsequentes dentro de 10 segundos usarão o Memcached ("Cache HIT").
