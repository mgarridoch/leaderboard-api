# 1. Imagen base: Empezamos con una imagen oficial de Python 3.11 ligera.
FROM python:3.11-slim

# 2. Directorio de trabajo: Establecemos el directorio donde se ejecutará nuestra app dentro del contenedor.
WORKDIR /app

# 2.1 Instalar dependencias del sistema: Algunas librerías de Python necesitan herramientas de compilación.
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev

# 3. Copiar e instalar dependencias: Copiamos solo el archivo de requerimientos primero.
COPY requirements.txt .

# -- La magia de la caché de Docker --
# Al instalar las dependencias en un paso separado, Docker reutilizará esta capa si no
# cambiamos 'requirements.txt', haciendo las futuras construcciones mucho más rápidas.
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código fuente: Ahora sí, copiamos el resto del código de nuestra app.
COPY . .

# 5. Comando de ejecución: Le decimos a Docker cómo iniciar nuestra aplicación.
# Usamos 0.0.0.0 para que la app sea accesible desde fuera del contenedor.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]