from pydantic import BaseModel
from datetime import datetime
import uuid

# Modelo base con los campos que se comparten
class ScoreBase(BaseModel):
    user_id: str
    score: int

# Modelo para recibir datos al crear un score (lo que viene en el POST)
class ScoreCreate(ScoreBase):
    pass

# Modelo completo que incluye los datos que genera el servidor (lo que devolvemos en la respuesta)
class Score(ScoreBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        # Permite que el modelo sea creado desde un objeto de base de datos 
        orm_mode = True