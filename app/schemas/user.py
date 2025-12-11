from pydantic import BaseModel, EmailStr

# 1. Kullanıcıdan Gelen Veri (Kayıt Olurken)
class UserCreate(BaseModel):
    email: EmailStr  # Email formatında olmak zorunda
    password: str
    full_name: str | None = None

# 2. Kullanıcıya Döneceğimiz Veri (Cevap Verirken)
# Şifreyi asla geri dönmeyiz! O yüzden burada password yok.
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    is_active: bool

    class Config:
        from_attributes = True  # Veritabanı modelini Pydantic modeline çevirmeyi sağlar