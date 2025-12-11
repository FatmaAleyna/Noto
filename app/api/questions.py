from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.ai_service import generate_questions_from_text

router = APIRouter()


@router.post("/generate-from-file")
async def generate_questions_file(file: UploadFile = File(...)):
    """
    Kullanıcıdan bir .txt dosyası alır, okur ve AI servisine gönderir.
    """
    # 1. Dosya tipini kontrol et (Sadece text dosyaları)
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Sadece .txt dosyaları desteklenmektedir.")

    # 2. Dosyanın içeriğini oku
    try:
        content = await file.read()
        # Dosyayı metne çevir (UTF-8)
        text_content = content.decode("utf-8")

        # Boş dosya kontrolü
        if len(text_content.strip()) < 50:
            raise HTTPException(status_code=400, detail="Dosya içeriği çok kısa veya boş.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Dosya okuma hatası: {str(e)}")

    # 3. Metni AI servisine gönder
    result = generate_questions_from_text(text_content)

    # 4. Sonucu kontrol et
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])

    return result