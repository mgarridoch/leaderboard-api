from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
import schemas
import crud
import security
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    description="Servicio para manejar usuarios y autenticación",
    version="0.1.0"
)

# 1. ESQUEMA DE SEGURIDAD
# Le dice a FastAPI dónde está el endpoint de login.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# 2. DEPENDENCIA DE SEGURIDAD
# Esta es una función reutilizable que podemos "inyectar" en cualquier endpoint que queramos proteger.
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    payload = security.decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido (sin 'sub')",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = crud.get_user_by_username(db, username=username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# --- Endpoints Públicos ---

@app.get("/")
def root():
    return {"service": "user-service", "status": "ok"}


@app.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = crud.create_user(db, user=user)
    return new_user


@app.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )
    
    access_token = security.create_access_token(
        data={"sub": user.username, "user_id": str(user.id)}
    )
    return {"access_token": access_token, "token_type": "bearer"}


# --- Endpoint Protegido ---

# Este endpoint solo es accesible con un token válido. Devuelve los datos del usuario actual.
@app.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user