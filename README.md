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

-   [x] **Fase 1: El Monolito Funcional**
    -   [x] Diseño del esquema de la base de datos (Usuarios, Puntuaciones).
    -   [x] Creación de la aplicación base con FastAPI.
    -   [x] Implementación de los endpoints principales de la API (enviar puntuación, obtener leaderboard).
    -   [x] Conexión a una base de datos PostgreSQL.
-   [x] **Fase 2: La "Dockerización"**
    -   [x] Escribir un `Dockerfile` para la aplicación FastAPI.
    -   [x] Asegurar que la aplicación pueda ser construida y ejecutada como un contenedor de Docker.
-   [ ] **Fase 3: La División (Microservicios)**
    -   [ ] Refactorizar el código en dos servicios: `user-service` y `leaderboard-service`.
    -   [ ] Establecer la comunicación entre los servicios (ej. llamadas HTTP directas).
-   [x] **Fase 4: La Orquestación**
    -   [x] Crear un archivo `docker-compose.yml` para gestionar la red de contenedores.
    -   [x] Configurar la base de datos como otro servicio dentro de Docker Compose.
    -   [x] Lograr que toda la aplicación (múltiples servicios + base de datos) se levante con un solo comando: `docker-compose up`.

***
## 📖 Documentación de la API (Endpoints)

*(Esta sección se completará durante la Fase 1)*

***
## 🚀 Cómo Empezar (con Docker)

Gracias a Docker, levantar todo el entorno de desarrollo es increíblemente simple. El único prerrequisito es tener **Docker Desktop** instalado.

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/mgarridoch/leaderboard-api.git](https://github.com/mgarridoch/leaderboard-api.git)
    cd leaderboard-api
    ```

2.  **Levanta los servicios:**
    Ejecuta el siguiente comando. La primera vez, Docker descargará la imagen de PostgreSQL y construirá la imagen de la API. Las veces siguientes, será casi instantáneo.
    ```bash
    docker-compose up
    ```
    *Si haces cambios en el `Dockerfile` o en `requirements.txt`, usa `docker-compose up --build` para forzar la reconstrucción de la imagen.*

3.  **¡Listo!** El servidor de la API y la base de datos ya están corriendo.
    -   La API está disponible en `http://localhost:8000`.
    -   La documentación interactiva para probar los endpoints está en **`http://localhost:8000/docs`**.

4.  **Para detener la aplicación:**
    Presiona `Ctrl + C` en la terminal donde ejecutaste el comando. Para asegurarte de que los contenedores se eliminen, puedes ejecutar:
    ```bash
    docker-compose down
    ```