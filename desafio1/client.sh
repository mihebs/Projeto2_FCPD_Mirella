#!/bin/sh
echo "Iniciando client..."
while true; do
    echo "Acessando servidor em http://server:8080..."
    curl -s http://server:8080
    echo "" # Quebra de linha para log mais limpo
    sleep 5
done
