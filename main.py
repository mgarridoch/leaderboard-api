from fastapi import FastAPI, status
from datetime import datetime
import uuid
from schemas import Score, ScoreCreate

# 1. Crear una instancia de FastAPI
app = FastAPI()

# 2. Definir el endpoint y su función
@app.get("/leaderboard")
def get_leaderboard():
    # 3. Mock de datos del leaderboard
    fake_leaderboard = {
        "leaderboard": [
            {
                "rank": 1,
                "user_id": "player_a4b1c",
                "score": 98500,
                "created_at": "2025-10-09T14:30:00Z",
            },
            {
                "rank": 2,
                "user_id": "player_d3f8e",
                "score": 98300,
                "created_at": "2025-10-04T11:22:00Z",
            },
        ]
    }
    return fake_leaderboard

# Post endpoint to create a new score
@app.post("/scores", response_model=Score, status_code=status.HTTP_201_CREATED)
def create_score(score_input: ScoreCreate):
    # Por ahora, como no hay base de datos, simulamos la creación
    print(f"Recibido puntaje para el usuario {score_input.user_id} de {score_input.score} puntos.")
    # 3. Creamos un objeto Score completo para la respuesta, añadiendo los datos del servidor
    new_score = Score(
        id=uuid.uuid4(),  # Genera un ID único
        user_id=score_input.user_id,
        score=score_input.score,
        created_at=datetime.utcnow() # Usa la hora actual en UTC
    )

    return new_score