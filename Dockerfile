# Usa una imagen base de Python 3.8 (puedes elegir otra versión si lo requieres)
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todos los archivos del repositorio a la imagen
COPY . /app

# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar las pruebas con pytest
CMD ["pytest", "test_api.py"]
