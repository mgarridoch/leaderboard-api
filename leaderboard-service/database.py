from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# 1. URL de conexión (la leeremos desde un archivo de configuración más adelante)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 2. El motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. La clase para las sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. La base para nuestros modelos ORM
Base = declarative_base()

# 5. Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()