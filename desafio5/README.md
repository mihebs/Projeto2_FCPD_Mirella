# Desafio 5: Microsserviços com API Gateway (HAProxy)

Este desafio implementa um padrão de API Gateway utilizando o **HAProxy** para rotear tráfego para diferentes microsserviços baseado na URL requisitada.

## Estrutura do Sistema

1.  **API Gateway (HAProxy):**
    *   Ponto único de entrada.
    *   Escuta na porta 80 (mapeada para 8080 no host).
    *   Roteia `/users` para o microsserviço de Usuários.
    *   Roteia `/orders` para o microsserviço de Pedidos.

2.  **Users API:**
    *   Serviço Python Flask simples retornando JSON de usuários.

3.  **Orders API:**
    *   Serviço Python Flask simples retornando JSON de pedidos.

## Decisão Técnica: HAProxy (The "Pro" Proxy)

Escolhemos o **HAProxy** (High Availability Proxy) em vez de soluções como Nginx ou um Gateway em Python por ser o padrão ouro da indústria para balanceamento de carga de alto desempenho.
*   **Especialização:** HAProxy é desenhado especificamente para performance e confiabilidade em roteamento TCP/HTTP.
*   **Observabilidade:** Possui uma página de status embutida (`/haproxy?stats`) excelente para monitoramento de SysAdmin.
*   **Configuração Declarativa:** O arquivo `haproxy.cfg` permite definir ACLs complexas de forma clara e concisa.

## Como Executar

1.  **Subir o Ambiente:**
    ```bash
    docker-compose up --build
    ```

2.  **Testar Rotas (Via Gateway):**
    *   Acessar Usuários: `http://localhost:8080/users` -> Deve retornar JSON da API de usuários.
    *   Acessar Pedidos: `http://localhost:8080/orders` -> Deve retornar JSON da API de pedidos.
    *   Verificar Estatísticas: `http://localhost:8080/haproxy?stats`
