from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services import user as user_service

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. Bu email daha önce alınmış mı kontrol et
    db_user = user_service.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı!")

    # 2. Kullanıcıyı oluştur
    return user_service.create_user(db=db, user=user_in)