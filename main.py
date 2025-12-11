from fastapi import FastAPI
from app.db.database import engine
from app.models import user
from app.api import users, questions, summary

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Router'ı dahil et (Prefix: Tüm user linkleri /users ile başlayacak)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(questions.router, prefix="/questions", tags=["Questions"])

app.include_router(summary.router, prefix="/summary", tags=["Summary"])

@app.get("/")
def read_root():
    return {"mesaj": "Noto Backend Çalışıyor! 🚀"}