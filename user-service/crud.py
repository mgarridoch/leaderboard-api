from sqlalchemy.orm import Session
import models
import schemas
import security 

# Busca un usuario por su nombre de usuario
def get_user_by_username(db: Session, username: str) -> models.User | None:
    return db.query(models.User).filter(models.User.username == username).first()

# Crea un nuevo usuario en la base de datos
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    # 1. Hashea la contraseña del usuario usando la función de 'security.py'
    hashed_password = security.get_password_hash(user.password)

    # 2. Crea una instancia del modelo 'models.User', pasando el 'username'
    db_user = models.User(username=user.username, hashed_password=hashed_password)

    # 3. Añade, comitea y refresca el nuevo usuario en la base de datos
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user