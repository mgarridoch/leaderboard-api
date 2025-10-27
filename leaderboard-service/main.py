from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from sqlalchemy.orm import Session
import httpx 
import os 
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# HTTPBearer() le dirá a /docs que solo pida el token
security_scheme = HTTPBearer()

# 2. Definimos la URL de nuestro servicio de usuarios
#    Usamos el nombre del servicio de Docker Compose: 'user-service'
#    y el puerto INTERNO del contenedor (8000).
USER_SERVICE_URL = "http://user_service:8000/users/me"

@app.get("/leaderboard")
def get_leaderboard(db: Session = Depends(get_db)):
    top_scores_models = db.query(models.Score).order_by(models.Score.score.desc()).limit(10).all()
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


# 3. Modificamos la firma de la función
@app.post("/scores", response_model=schemas.Score, status_code=status.HTTP_201_CREATED)
def create_score(
    score_input: schemas.ScoreCreate, 
    db: Session = Depends(get_db), 
    # --- MODIFICADO: Usamos el nuevo 'scheme' y tipo de credencial ---
    creds: HTTPAuthorizationCredentials = Depends(security_scheme)
):
    
    token = creds.credentials
    
    headers = {"Authorization": f"Bearer {token}"}
    try:
        with httpx.Client() as client:
            response = client.get(USER_SERVICE_URL, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado"
            )
        
        user_data = response.json()
        user_id = user_data["id"]

    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No se pudo conectar con el servicio de autenticación"
        )

    # El resto de la función (guardar en BD) es igual
    new_score = models.Score(
        user_id=user_id,
        score=score_input.score
    )
    
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    
    return new_score