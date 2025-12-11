from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Bağlantı Adresi (Connection String)
# Format: postgresql://kullanici:sifre@adres:port/veritabani_adi
SQLALCHEMY_DATABASE_URL = "postgresql://noto_user:supergizlisifre@localhost:5432/noto_database"

# 2. Motoru Çalıştır (Engine)
# Bu, veritabanı ile Python arasındaki kapıyı açar.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Oturum Oluşturucu (SessionLocal)
# Her istek geldiğinde veritabanıyla konuşacak geçici bir oturum açar.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Temel Model Sınıfı (Base)
# Veritabanı tablolarımızı bu sınıftan türeteceğiz.
Base = declarative_base()

# 5. Veritabanı Bağlantısı Al (Dependency)
# Bunu API fonksiyonlarında kullanacağız ("Bana bir veritabanı oturumu ver" demek için)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()