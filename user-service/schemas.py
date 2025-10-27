from pydantic import BaseModel
import uuid

# Schema para recibir datos al crear un usuario
class UserCreate(BaseModel):
    username: str
    password: str

# Schema para devolver datos de un usuario (NUNCA devolver la contraseña)
class User(BaseModel):
    id: uuid.UUID
    username: str

    class Config:
        from_attributes = True