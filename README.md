# API Flask com Docker

Este é um projeto simples de uma API feita em Python usando Flask, containerizada com Docker.

## Funcionalidades

- `GET /` — Retorna uma mensagem de status.
- `GET /soma?a=5&b=3` — Retorna a soma de dois números passados via query params.

## Como executar com Docker

```bash
# Build da imagem
docker build -t minha-api-python .

# Executa o container
docker run -p 5000:5000 minha-api-python

#Exemplo de uso
Acesse: http://localhost:5000

#Estrutura do Projeto
meu-api-python/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

#Autor
Projeto criado por João com auxilio do ChatGPT.
