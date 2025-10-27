# 🏆 Leaderboard API Service

Un proyecto de portafolio enfocado en construir un servicio de backend escalable, robusto y listo para la nube para un sistema de tablas de clasificación (leaderboards) de videojuegos.

El objetivo principal es demostrar habilidades en diseño de API REST, arquitectura de microservicios, containerización con Docker y buenas prácticas de ingeniería de backend.

## ✨ Características Implementadas
* Envío de puntuaciones de jugadores.
* Recuperación del Top 10 de jugadores (leaderboard global).
* Entorno de desarrollo y producción completamente "dockerizado" con persistencia de datos.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.11+
* **Framework API:** FastAPI
* **Base de Datos:** PostgreSQL
* **ORM:** SQLAlchemy
* **Containerización:** Docker & Docker Compose

***
## 🗺️ Roadmap de Desarrollo

Este proyecto se construyó de manera incremental siguiendo estas fases:

-   [x] **Fase 1: El Monolito Funcional**
    -   [x] Diseño del esquema de la base de datos (Usuarios, Puntuaciones).
    -   [x] Creación de la aplicación base con FastAPI.
    -   [x] Implementación de los endpoints principales de la API (enviar puntuación, obtener leaderboard).
    -   [x] Conexión a una base de datos PostgreSQL.
-   [x] **Fase 2: La "Dockerización"**
    -   [x] Escribir un `Dockerfile` para la aplicación FastAPI.
    -   [x] Asegurar que la aplicación pueda ser construida y ejecutada como un contenedor de Docker.
-   [x] **Fase 3: La División (Microservicios)**
    -   [x] Refactorizar el código en dos servicios: `user-service` y `leaderboard-service`.
    -   [x] Establecer la comunicación entre los servicios (ej. llamadas HTTP directas).
-   [x] **Fase 4: La Orquestación**
    -   [x] Crear un archivo `docker-compose.yml` para gestionar la red de contenedores.
    -   [x] Configurar la base de datos como otro servicio dentro de Docker Compose.
    -   [x] Lograr que toda la aplicación (múltiples servicios + base de datos) se levante con un solo comando: `docker-compose up`.

***
## 📖 Documentación de la API (Endpoints)

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| **`POST`** | `/scores` | Envía un nuevo puntaje. El cuerpo debe ser un JSON con `user_id` (string) y `score` (int). |
| **`GET`** | `/leaderboard` | Recupera un objeto que contiene una lista con el Top 10 de puntajes de la clasificación. |

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

***
## 🧠 Principales Aprendizajes
Este proyecto sirvió como una implementación práctica de varios conceptos clave del desarrollo backend moderno:

* **FastAPI:** Uso de Pydantic (`schemas.py`) para la validación automática de datos de entrada y serialización de salida (`response_model`). Implementación del patrón de Inyección de Dependencias (`Depends`) para gestionar las sesiones de la base de datos de forma limpia.
* **SQLAlchemy:** Definición de modelos de datos (`models.py`) que se traducen en tablas de PostgreSQL. Creación de la conexión (`engine`) y el patrón de sesión (`SessionLocal`, `get_db`) para interactuar con la base de datos. Escritura de consultas ORM (`db.query`, `.order_by`, `.limit`).
* **Docker:** Creación de un `Dockerfile` optimizado que aprovecha la caché de capas de Docker (instalando `requirements.txt` en un paso separado). Resolución de problemas de dependencias (`psycopg2` vs `psycopg2-binary`) específicos del entorno del contenedor.
* **Docker Compose:** Orquestación de una aplicación multi-contenedor (`api` y `db`). Configuración de una red interna (permitiendo a la API contactar a la BD a través del nombre de host `db`). Gestión de la persistencia de datos de la base de datos usando volúmenes (`volumes`).
* **Desarrollo Local:** Configuración de "hot-reloading" (recarga en caliente) dentro de un contenedor de Docker usando volúmenes (`.:/app`) para un flujo de desarrollo rápido.

***
## 🔮 Mejoras a Futuro
Aunque el proyecto es funcional, tiene un gran potencial para crecer y demostrar habilidades más avanzadas:

* **Funcionalidad:**
    * **Endpoint de Usuario:** Crear `GET /scores/{user_id}` para ver el puntaje y el ranking de un jugador específico.
    * **Paginación:** Mejorar `GET /leaderboard` para que acepte parámetros de consulta (`?limit=50&offset=0`) y poder navegar por clasificaciones grandes.
    * **Validación Avanzada:** Añadir validación para que no se puedan enviar puntajes negativos o `user_id` vacíos.
* **Seguridad:**
    * **Autenticación:** Implementar un sistema de autenticación (ej. con JWT) para que solo los usuarios registrados puedan enviar puntajes (`POST /scores`).
* **Arquitectura:**
    * **Microservicios:** Ejecutar la **Fase 3** del roadmap, separando la lógica en un `user-service` (para manejar la autenticación) y un `leaderboard-service`.
    * **Caching:** Añadir una capa de caché con **Redis** al endpoint `GET /leaderboard` para reducir la carga en la base de datos y mejorar drásticamente los tiempos de respuesta.
* **Pruebas (Testing):**
    * Implementar una suite de pruebas unitarias y de integración usando `pytest` para garantizar la fiabilidad del código.