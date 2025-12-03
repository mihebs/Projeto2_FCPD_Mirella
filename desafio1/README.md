# Desafio 1: Containers em Rede

Este desafio demonstra a comunicação entre dois containers (Cliente e Servidor) dentro de uma rede Docker personalizada chamada `infra_net_v1`.

## Estrutura do Desafio

*   **Servidor:** Um container Python simples servindo arquivos estáticos.
*   **Cliente:** Um container Alpine Linux rodando um script Shell que faz requisições periódicas ao servidor.

## Decisões Técnicas

### Por que `http.server`?
Escolhemos o módulo nativo `http.server` do Python para o container servidor pela sua **extrema simplicidade e eficiência** para este caso de uso.
*   **Minimalismo:** Não requer frameworks externos como Flask ou Django, reduzindo o tamanho da imagem e a superfície de ataque.
*   **Propósito:** O objetivo era apenas servir conteúdo estático e comprovar a conectividade de rede. O `http.server` cumpre isso perfeitamente sem "boilerplate" code.
*   **Disponibilidade:** Já vem instalado com o Python, facilitando o setup imediato.

### Script Client (`client.sh`)
O cliente foi implementado como um script Shell rodando em Alpine Linux para demonstrar uma abordagem de **SysAdmin**. Em vez de escrever um cliente em Python/Node, usamos ferramentas nativas de sistema (`curl`, `sh`) que são leves e onipresentes em ambientes de infraestrutura.

## Como Executar

1.  **Criar a rede:**
    ```bash
    docker network create infra_net_v1
    ```

2.  **Build das Imagens:**
    ```bash
    docker build -t desafio1-server -f Dockerfile.server .
    docker build -t desafio1-client -f Dockerfile.client .
    ```

3.  **Rodar o Servidor:**
    ```bash
    docker run -d --name server --network infra_net_v1 desafio1-server
    ```

4.  **Rodar o Cliente:**
    ```bash
    docker run --name client --network infra_net_v1 desafio1-client
    ```

5.  **Verificar Logs:**
    Você verá o cliente acessando o servidor a cada 5 segundos.
