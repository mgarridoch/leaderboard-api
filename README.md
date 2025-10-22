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
    -   [ ] Diseño del esquema de la base de datos (Usuarios, Puntuaciones).
    -   [ ] Creación de la aplicación base con FastAPI.
    -   [ ] Implementación de los endpoints principales de la API (enviar puntuación, obtener leaderboard).
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

*(Instrucciones detalladas se añadirán al completar la Fase 2: Dockerización)*