# Usa una imagen base ligera de Python 3.10.9
FROM python:3.10.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el requirements.txt e instala dependencias
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala dependencias del sistema necesarias para PostgreSQL y zona horaria
RUN apt-get update && apt-get install -y \
    libpq-dev \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia el resto de los archivos de la app
COPY . .

# Copia el entrypoint y le da permisos
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Define el script de entrada por defecto
ENTRYPOINT ["/entrypoint.sh"]

# Comando por defecto (puede sobrescribirse en docker-compose o CLI)
# Editar según el tipo de aplicación (WSGI con gunicorn o ASGI con uvicorn)
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8001"]
