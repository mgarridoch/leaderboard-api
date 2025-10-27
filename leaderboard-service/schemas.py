from pydantic import BaseModel
from datetime import datetime
import uuid

# 'ScoreBase' ahora solo contiene el puntaje
class ScoreBase(BaseModel):
    score: int

# 'ScoreCreate' hereda de 'ScoreBase', por lo que solo espera 'score'
class ScoreCreate(ScoreBase):
    pass

# 'Score' es nuestro modelo de respuesta, que sí incluye el 'user_id'
class Score(ScoreBase):
    id: uuid.UUID
    created_at: datetime
    user_id: str  

    class Config:
        from_attributes = True