FROM python:3.13-slim

# Define o diretório de trabalho dentro do container
WORKDIR /parking_service

# Evita criação de arquivos .pyc e ativa logs sem buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Atualiza pacotes e instala dependências do sistema (inclusive para Playwright)
RUN apt update && apt install -y \
    build-essential \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxss1 \
    libxtst6 \
    libxcb1 \
    libx11-6 \
    libglib2.0-0 \
    libgdk-pixbuf2.0-0 \
    libfontconfig1 \
    libcairo2 \
    curl \
    wget \
    unzip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto para dentro do container
COPY . .

# Atualiza o pip
RUN pip install --upgrade pip

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Instala os navegadores necessários para o Playwright (ex: Chromium, Firefox, WebKit)
RUN playwright install --with-deps

# Expõe a porta padrão do Django
EXPOSE 8000
