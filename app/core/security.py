from passlib.context import CryptContext

# Şifreleme ayarları (bcrypt kullanıyoruz)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# 1. Şifreyi Hash'le (Gizle)
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 2. Şifreyi Doğrula (Giriş yaparken lazım olacak)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)