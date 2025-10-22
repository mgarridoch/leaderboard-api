# 🏆 Leaderboard API Service

Un proyecto de portafolio enfocado en construir un servicio de backend escalable, robusto y listo para la nube para un sistema de tablas de clasificación (leaderboards) de videojuegos.

El objetivo principal es demostrar habilidades en diseño de API REST, arquitectura de microservicios, containerización con Docker y buenas prácticas de ingeniería de backend.

## ✨ Características Principales (a Implementar)
* Envío de puntuaciones de jugadores.
* Recuperación del Top N de jugadores (leaderboard global).
* Consulta del ranking de un jugador específico.
* Entorno de desarrollo y producción completamente "dockerizado".
* Arquitectura distribuida con múltiples servicios comunicándose entre sí.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.11+
* **Framework API:** FastAPI
* **Base de Datos:** PostgreSQL
* **Containerización:** Docker & Docker Compose

***
## 🗺️ Roadmap de Desarrollo

Este proyecto se construirá de manera incremental siguiendo estas fases:

-   [ ] **Fase 1: El Monolito Funcional**
    -   [x] Diseño del esquema de la base de datos (Usuarios, Puntuaciones).
    -   [x] Creación de la aplicación base con FastAPI.
    -   [x] Implementación de los endpoints principales de la API (enviar puntuación, obtener leaderboard).
    -   [ ] Conexión a una base de datos PostgreSQL.
-   [ ] **Fase 2: La "Dockerización"**
    -   [ ] Escribir un `Dockerfile` para la aplicación FastAPI.
    -   [ ] Asegurar que la aplicación pueda ser construida y ejecutada como un contenedor de Docker.
-   [ ] **Fase 3: La División (Microservicios)**
    -   [ ] Refactorizar el código en dos servicios: `user-service` y `leaderboard-service`.
    -   [ ] Establecer la comunicación entre los servicios (ej. llamadas HTTP directas).
-   [ ] **Fase 4: La Orquestación**
    -   [ ] Crear un archivo `docker-compose.yml` para gestionar la red de contenedores.
    -   [ ] Configurar la base de datos como otro servicio dentro de Docker Compose.
    -   [ ] Lograr que toda la aplicación (múltiples servicios + base de datos) se levante con un solo comando: `docker-compose up`.

***
## 📖 Documentación de la API (Endpoints)

*(Esta sección se completará durante la Fase 1)*

***
## 🚀 Cómo Empezar (Localmente)

Para levantar el servidor en tu máquina local, necesitarás tener **Python 3.11+** instalado. Sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    cd leaderboard-api
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crea el entorno
    python -m venv venv

    # Actívalo
    # En Windows: .\venv\Scripts\activate
    # En macOS/Linux: source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el servidor:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **¡Listo!** El servidor estará corriendo en `http://127.0.0.1:8000`.
    -   Puedes ver el endpoint del leaderboard en `http://127.0.0.1:8000/leaderboard`.
    -   La documentación interactiva de la API está en `http://127.0.0.1:8000/docs`.