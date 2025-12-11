from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    # 1. Şifreyi Hash'le (Gizle)
    hashed_password = get_password_hash(user.password)

    # 2. Veritabanı objesini hazırla
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )

    # 3. Veritabanına ekle ve kaydet
    db.add(db_user)
    db.commit()

    # 4. Kaydedilen veriyi geri getir (ID'si oluşmuş haliyle)
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()