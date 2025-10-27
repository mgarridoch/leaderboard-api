from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

# --- Configuración de Seguridad ---
# Es MUY importante que estas claves sean secretas y se lean desde variables de entorno en producción.
SECRET_KEY = "secret-change-me" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 1. Contexto para Hashear Contraseñas
# Le dice a passlib que use argon2 como el algoritmo de hash
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# --- Funciones de Contraseña ---

# Verifica una contraseña en texto plano contra un hash guardado
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Genera un hash para una contraseña en texto plano.
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# --- Funciones de Token JWT ---

# Crea un token JWT con los datos proporcionados
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decodifica un token JWT. Devuelve el payload (los datos) si es válido, o None si es inválido.
def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None