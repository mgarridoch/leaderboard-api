from fastapi import FastAPI, status, Depends
from datetime import datetime
import uuid
from schemas import Score, ScoreCreate
import models
from database import engine, get_db
from sqlalchemy.orm import Session
import schemas

# 0. Crear las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

# 1. Crear una instancia de FastAPI
app = FastAPI()

# 2. Definir el endpoint y su función
@app.get("/leaderboard") # <-- Puedes añadir un response_model si quieres
def get_leaderboard(db: Session = Depends(get_db)):    
    # 1. Obtenemos los 10 mejores puntajes de la BD
    top_scores_models = db.query(models.Score).order_by(models.Score.score.desc()).limit(10).all()

    # 2. Creamos la lista de diccionarios para nuestra respuesta
    leaderboard = []
    for i, model in enumerate(top_scores_models):
        leaderboard.append({
            "rank": i + 1,
            "id": model.id,
            "user_id": model.user_id,
            "score": model.score,
            "created_at": model.created_at
        })

    return { "leaderboard": leaderboard }

# Post endpoint to create a new score
@app.post("/scores", response_model=Score, status_code=status.HTTP_201_CREATED)
def create_score(score_input: schemas.ScoreCreate, db: Session = Depends(get_db)):
    new_score = models.Score(
        user_id=score_input.user_id,
        score=score_input.score
    )
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    return new_score