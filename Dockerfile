# Imagem base
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expor a porta da API
EXPOSE 5000

# Comando para rodar a API
CMD ["python", "app.py"]
