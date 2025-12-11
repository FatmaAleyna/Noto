from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.ai_service import generate_summary_from_text

router = APIRouter()


@router.post("/generate-from-file")
async def generate_summary_file(file: UploadFile = File(...)):
    """
    Dosyayı alır ve ÖZET çıkarır.
    """
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Sadece .txt dosyaları.")

    content = await file.read()
    text_content = content.decode("utf-8")

    if len(text_content.strip()) < 50:
        raise HTTPException(status_code=400, detail="Dosya çok kısa.")

    # Servise gönder (ÖZET FONKSİYONU)
    result = generate_summary_from_text(text_content)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error", "Bilinmeyen hata"))

    return result