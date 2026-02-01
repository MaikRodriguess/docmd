# Imagem base Python 3.11
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação
COPY . .

# Cria diretório para uploads
RUN mkdir -p uploads

# Expõe porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
