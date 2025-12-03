# Projeto 2 - Desafios com Docker

Este repositório contém a resolução do "Projeto 2 - Docker e Microsserviços", da disciplina Fundamentos de Computação Concorrente, Paralela e Distribuída.

## Desafios

Abaixo estão os links para a documentação detalhada de cada desafio implementado:

*   **[Desafio 1: Containers em Rede](./desafio1/README.md)**
    *   Foco: Networking Manual (`docker network`).
    *   Destaque: Uso de `python -m http.server` e script Client em Shell/Alpine.

*   **[Desafio 2: Volumes e Persistência](./desafio2/README.md)**
    *   Foco: Persistência de dados (`docker volume`).
    *   Destaque: Script de Log Storage escrevendo em disco local persistente.

*   **[Desafio 3: Orquestração com Docker Compose](./desafio3/README.md)**
    *   Foco: Orquestração de múltiplos serviços.
    *   Stack "Legacy": Flask + **MySQL** + **Memcached**.

*   **[Desafio 4: Microsserviços Independentes](./desafio4/README.md)**
    *   Foco: Comunicação Service-to-Service direta.
    *   Cenário: Catálogo de Livros e Display de Biblioteca.

*   **[Desafio 5: Microsserviços com API Gateway](./desafio5/README.md)**
    *   Foco: Padrão Gateway / Reverse Proxy.
    *   Destaque: Uso profissional do **HAProxy** para roteamento de requisições.

## Como Executar

Navegue até a pasta de cada desafio e siga as instruções no `README.md` local. A maioria dos desafios utiliza `docker-compose` ou comandos `docker build/run` padrão.
