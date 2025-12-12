# Noto – AI-Powered Educational Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
</p>

<p align="center">
  <strong>Eğitim içeriklerini anlayan, özetleyen ve sınav sorularına dönüştüren yapay zekâ platformu</strong>
</p>

---

## 📖 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Mimari Yapı](#-mimari-yapı-hybrid-microservices)
- [Teknoloji Stack](#-teknoloji-stack)
- [Proje Yapısı](#-proje-yapısı)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [API Endpoints](#-api-endpoints)
- [AI Worker Kurulumu](#-ai-worker-kurulumu-google-colab)
- [Konfigürasyon](#-konfigürasyon)
- [Güvenlik](#-güvenlik)
- [Geliştirme](#-geliştirme)
- [Sorun Giderme](#-sorun-giderme)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🚀 Proje Hakkında

**Noto**, eğitim içeriklerini yapay zeka ile analiz ederek öğrenciler ve eğitimciler için otomatik soru ve özet üreten modern bir backend platformudur. Türkçe diline özel optimize edilmiş LLM modelleri kullanarak:

- 📝 **Otonom sınav soruları** üretir (klasik ve test soruları)
- 📚 **Kapsamlı özetler** çıkarır
- 🧠 **Bloom taksonomisi** ile uyumlu sorular oluşturur
- ⚡ **Hibrit mimari** sayesinde hızlı ve maliyet etkin çalışır

Proje, **FastAPI** ile geliştirilmiş RESTful API ve **Google Colab** üzerinde çalışan AI Worker'dan oluşan iki katmanlı bir mikroservis mimarisine sahiptir.

---

## ✨ Özellikler

### 🎯 Soru Üretimi
- **Klasik/Teorik Sorular**: Kavramsal derinlik gerektiren açık uçlu sorular
- **Çoktan Seçmeli Sorular**: 5 seçenekli test soruları
- **Zorluk Seviyelendirme**: Akademik düzeyde, Bloom taksonomisine uygun
- **Few-Shot Learning**: Örnek bazlı prompt engineering

### 📘 Akıllı Özetleme
- Anlam bütünlüğü korunarak özet çıkarma
- Temel fikirleri, argümanları ve kritik noktaları yakalama
- Akademik terminoloji desteği
- 700 token'a kadar kapsamlı özetler

### 🔐 Kullanıcı Yönetimi
- Güvenli kullanıcı kaydı (Argon2 şifreleme)
- E-posta doğrulama
- PostgreSQL tabanlı veri saklama
- SQLAlchemy ORM entegrasyonu

### 🌐 Hibrit Mimari
- **Yerel API**: Kullanıcı verileri ve iş mantığı lokal sunucuda
- **Cloud GPU**: AI hesaplamaları Google Colab'da
- **Güvenli Tünel**: Cloudflare Tunnel ile şifreli iletişim
- **Maliyet Optimizasyonu**: %80'e varan maliyet tasarrufu

---

## 🏗 Mimari Yapı: Hybrid Microservices

Noto, **veri güvenliği** ve **maliyet optimizasyonu** için özel olarak tasarlanmış hibrit mikroservis mimarisi kullanır:

### Mimari Diyagram

```
┌─────────────────────┐
│   Kullanıcı/Client  │
│    (Web/Mobile)     │
└──────────┬──────────┘
           │ HTTP/JSON
           ▼
┌─────────────────────────────────┐
│   FastAPI Backend (Local)       │
│   • User Management             │
│   • File Upload/Validation      │
│   • Request Routing             │
│   • Response Formatting         │
└──────────┬──────────────────────┘
           │ SQL
           ▼
┌─────────────────────────────────┐
│    PostgreSQL Database          │
│    • User Data                  │
│    • Session Management         │
└─────────────────────────────────┘
           │
           │ Cloudflare Tunnel (HTTPS)
           ▼
┌─────────────────────────────────┐
│   AI Worker (Google Colab)      │
│   • GPU Inference               │
│   • Trendyol-LLM-7B Model       │
│   • Question Generation         │
│   • Summary Generation          │
└─────────────────────────────────┘
```

### Neden Hibrit?

| Bileşen | Konum | Açıklama | Avantaj |
|---------|-------|----------|---------|
| **API & İş Mantığı** | Local (On-Premise) | Kullanıcı verileri ve kritik iş mantığı | Veri güvenliği, düşük gecikme |
| **AI Hesaplamaları** | Cloud GPU (Colab) | Ağır LLM inference işlemleri | GPU erişimi, ölçeklenebilirlik |
| **Veritabanı** | Local (Docker) | PostgreSQL container | Veri kontrolü, hızlı erişim |
| **İletişim** | Cloudflare Tunnel | API ↔ AI Worker bağlantısı | Güvenli, şifreli, NAT bypass |

---

## 🛠 Teknoloji Stack

### Backend Framework
- **FastAPI** - Modern, hızlı web framework (async support)
- **Uvicorn** - ASGI server (production-ready)
- **Pydantic** - Veri validasyonu ve type checking

### Database & ORM
- **PostgreSQL 15** - İlişkisel veritabanı
- **SQLAlchemy** - Python ORM
- **Docker Compose** - Veritabanı containerization

### Security
- **Passlib** - Şifre hashing kütüphanesi
- **Argon2** - Şifre hashing algoritması (GPU saldırılarına dirençli)
- **Email-Validator** - E-posta doğrulama

### AI & Machine Learning
- **Hugging Face Transformers** - Model yükleme ve inference
- **PyTorch** - Deep learning framework
- **Trendyol-LLM-7B-chat-dpo-v1.0** - Türkçe optimize LLM modeli
- **Bitsandbytes** - GPU optimizasyonu
- **Accelerate** - Dağıtık inference

### Infrastructure
- **Docker** - Containerization
- **Cloudflare Tunnel** - Güvenli tünel
- **Google Colab** - Cloud GPU platform

### Development Tools
- **Python 3.9+** - Programlama dili
- **Git** - Versiyon kontrolü
- **PyCharm/VS Code** - IDE

---

## 📁 Proje Yapısı

```
Noto_Backend/
│
├── app/                              # Ana uygulama paketi
│   ├── __init__.py
│   │
│   ├── api/                          # API endpoint handlers
│   │   ├── __init__.py
│   │   ├── users.py                  # Kullanıcı kayıt/yönetim endpoints
│   │   ├── questions.py              # Soru üretimi endpoints
│   │   └── summary.py                # Özet üretimi endpoints
│   │
│   ├── core/                         # Çekirdek utilities
│   │   ├── __init__.py
│   │   └── security.py               # Şifre hashing/verification
│   │
│   ├── db/                           # Veritabanı konfigürasyonu
│   │   ├── __init__.py
│   │   └── database.py               # SQLAlchemy setup & session
│   │
│   ├── models/                       # SQLAlchemy ORM modelleri
│   │   ├── __init__.py
│   │   └── user.py                   # User database model
│   │
│   ├── schemas/                      # Pydantic validation schemas
│   │   ├── __init__.py
│   │   └── user.py                   # User request/response schemas
│   │
│   └── services/                     # İş mantığı servisleri
│       ├── __init__.py
│       ├── user.py                   # User service logic
│       └── ai_service.py             # AI Worker iletişimi
│
├── main.py                           # FastAPI uygulama entry point
├── docker-compose.yml                # PostgreSQL container tanımı
├── requirements.txt                  # Python dependencies
├── Noto_AI_Worker.ipynb             # Google Colab AI worker notebook
├── test_ai.py                        # AI service test scripti
├── .gitignore                        # Git ignore rules
├── .env.example                      # Örnek environment variables
└── README.md                         # Proje dokümantasyonu
```

### Klasör Açıklamaları

- **`app/api/`**: RESTful API endpoint'lerini tanımlar. Her modül bir router içerir.
- **`app/core/`**: Güvenlik, config gibi core fonksiyonlar.
- **`app/db/`**: Veritabanı bağlantı ve session yönetimi.
- **`app/models/`**: Database tablolarının SQLAlchemy model tanımları.
- **`app/schemas/`**: API request/response için Pydantic validation modelleri.
- **`app/services/`**: İş mantığı katmanı (API ↔ Database/AI Worker arası).

---

## 📦 Kurulum

### Gereksinimler

- **Python 3.9+**
- **Docker & Docker Compose**
- **Git**
- **Google Colab Hesabı** (AI Worker için)

### 1️⃣ Repository'yi Klonlayın

```bash
git clone https://github.com/FatmaAleyna/Noto.git
cd Noto_Backend
```

### 2️⃣ Virtual Environment Oluşturun (Önerilen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Dependencies Yükleyin

```bash
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic[email] passlib[argon2] requests python-multipart
```

> **Not**: `requirements.txt` güncellenecektir. Şimdilik manuel yükleme yapılmalıdır.

### 4️⃣ PostgreSQL Veritabanını Başlatın

```bash
docker-compose up -d
```

Bu komut, `noto_db` container'ını oluşturur ve PostgreSQL'i başlatır:
- **Database**: `noto_database`
- **User**: `noto_user`
- **Password**: `supergizlisifre`
- **Port**: `5432`

### 5️⃣ Veritabanı Bağlantısını Doğrulayın

```bash
docker ps  # Container'ın çalıştığını kontrol edin
```

### 6️⃣ Backend API'yi Başlatın

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API şu adreste çalışacak: **http://localhost:8000**

### 7️⃣ API Dokümantasyonunu Görüntüleyin

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🎮 Kullanım

### API Test Etme

#### 1. Kullanıcı Kaydı

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123",
    "full_name": "Test User"
  }'
```

**Yanıt:**
```json
{
  "id": 1,
  "email": "test@example.com",
  "full_name": "Test User",
  "is_active": true
}
```

#### 2. Soru Üretimi (AI Worker aktif olmalı)

```bash
curl -X POST "http://localhost:8000/questions/generate-from-file" \
  -F "file=@ders_notu.txt"
```

**Yanıt:**
```json
{
  "success": true,
  "klasik_soru": "Photosynthesis sürecinin oksijen üretimine katkısını açıklayınız...",
  "test_sorusu": "Aşağıdakilerden hangisi photosynthesis için gerekli değildir? A) Su B) CO2..."
}
```

#### 3. Özet Üretimi

```bash
curl -X POST "http://localhost:8000/summary/generate-from-file" \
  -F "file=@makale.txt"
```

**Yanıt:**
```json
{
  "success": true,
  "ozet": "Bu metin, yapay zeka ve makine öğrenmesi alanındaki son gelişmeleri..."
}
```

### Python ile Kullanım

```python
import requests

# Dosyadan soru üret
url = "http://localhost:8000/questions/generate-from-file"
files = {"file": open("ders_notu.txt", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

---

## 📡 API Endpoints

### Kullanıcı Yönetimi

| Method | Endpoint | Açıklama | Request Body | Response |
|--------|----------|----------|--------------|----------|
| `POST` | `/users/register` | Yeni kullanıcı kaydı | `UserCreate` | `UserOut` |

**UserCreate Schema:**
```json
{
  "email": "user@example.com",
  "password": "string",
  "full_name": "string (optional)"
}
```

**UserOut Schema:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "string",
  "is_active": true
}
```

### Soru Üretimi

| Method | Endpoint | Açıklama | Request | Response |
|--------|----------|----------|---------|----------|
| `POST` | `/questions/generate-from-file` | Metin dosyasından soru üret | `.txt` file | `QuestionResponse` |

**QuestionResponse Schema:**
```json
{
  "success": true,
  "klasik_soru": "Open-ended question...",
  "test_sorusu": "Multiple-choice question with 5 options..."
}
```

**Validasyonlar:**
- Dosya formatı: `.txt` olmalı
- Minimum metin uzunluğu: 50 karakter
- AI Worker: Aktif olmalı

### Özet Üretimi

| Method | Endpoint | Açıklama | Request | Response |
|--------|----------|----------|---------|----------|
| `POST` | `/summary/generate-from-file` | Metin dosyasından özet üret | `.txt` file | `SummaryResponse` |

**SummaryResponse Schema:**
```json
{
  "success": true,
  "ozet": "Generated summary text..."
}
```

### Sistem

| Method | Endpoint | Açıklama | Response |
|--------|----------|----------|----------|
| `GET` | `/` | Health check | `{"mesaj": "Noto Backend Çalışıyor! 🚀"}` |

---

## 🤖 AI Worker Kurulumu (Google Colab)

AI Worker, soru ve özet üretimi için GPU kullanarak LLM modelini çalıştırır. Google Colab'da ücretsiz GPU ile kurulabilir.

### Adım 1: Notebook'u Açın

1. **`Noto_AI_Worker.ipynb`** dosyasını Google Colab'da açın
2. Runtime → Change runtime type → **GPU** (T4 önerilir)

### Adım 2: Cell'leri Sırayla Çalıştırın

#### Cell 1: Kütüphane Kurulumu
```python
# transformers, torch, cloudflared kurulumu
!pip install -q transformers torch accelerate bitsandbytes
!wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
!chmod +x cloudflared
```

#### Cell 2: Model Yükleme (7B parametre - ~5-10 dakika)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Trendyol/Trendyol-LLM-7b-chat-dpo-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
```

#### Cell 7: FastAPI Server & Cloudflare Tunnel
Bu cell çalıştırıldığında:
1. FastAPI server başlar
2. Cloudflare tunnel otomatik oluşturulur
3. **Public URL** ekrana yazdırılır

**Çıktı örneği:**
```
======================================
AI WORKER HAZIR!
Cloudflare URL: https://formatting-drill-pizza-outstanding.trycloudflare.com
======================================
```

### Adım 3: Backend'e URL'i Ekleyin

Cloudflare URL'ini kopyalayın ve backend'deki `app/services/ai_service.py` dosyasında güncelleyin:

```python
# ai_service.py
BASE_AI_URL = "https://your-cloudflare-url.trycloudflare.com"
```

Alternatif olarak `.env` dosyası kullanın:
```bash
AI_SERVICE_URL=https://your-cloudflare-url.trycloudflare.com
```

### Adım 4: Test Edin

```bash
curl http://localhost:8000/questions/generate-from-file \
  -F "file=@test.txt"
```

> **Not**: Colab session kapandığında tunnel da kapanır. Yeniden başlatmak gerekir.

---

## ⚙️ Konfigürasyon

### Environment Variables (.env)

`.env.example` dosyasını `.env` olarak kopyalayın:

```bash
# Database
DATABASE_URL=postgresql://noto_user:supergizlisifre@localhost:5432/noto_database

# AI Worker
AI_SERVICE_URL=https://your-cloudflare-tunnel-url.trycloudflare.com

# Security (opsiyonel - gelecek özellikler için)
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Docker Compose Ayarları

`docker-compose.yml` dosyasında PostgreSQL ayarlarını değiştirebilirsiniz:

```yaml
environment:
  POSTGRES_USER: your_user
  POSTGRES_PASSWORD: your_password
  POSTGRES_DB: your_database
```

> **Dikkat**: Değişiklik yaparsanız `app/db/database.py` dosyasındaki connection string'i de güncelleyin.

### Database Connection String

`app/db/database.py`:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://noto_user:supergizlisifre@localhost:5432/noto_database"
```

---

## 🔒 Güvenlik

### Mevcut Güvenlik Önlemleri

1. **Şifre Hashing**: Argon2id algoritması (GPU saldırılarına dirençli)
2. **E-posta Validasyonu**: Pydantic EmailStr kullanımı
3. **SQL Injection Koruması**: SQLAlchemy ORM
4. **Şifreli Tünel**: Cloudflare Tunnel (HTTPS)
5. **Container İzolasyonu**: Docker ile veritabanı izolasyonu

### Önerilen Geliştirmeler (Production için)

- [ ] JWT token authentication implementasyonu
- [ ] HTTPS/SSL sertifikası (production deployment)
- [ ] Rate limiting (DDoS koruması)
- [ ] CORS policy konfigürasyonu
- [ ] Environment variable'ları `.env` dosyasına taşıma
- [ ] Database şifresini güçlendirme
- [ ] Input sanitization ekstra katmanları
- [ ] API key authentication (AI Worker için)

### Hassas Bilgilerin Korunması

```bash
# .gitignore dosyasına ekleyin
.env
*.db
__pycache__/
*.pyc
venv/
```

---

## 🧪 Geliştirme

### Development Mode

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

- `--reload`: Kod değişikliklerinde otomatik yeniden başlatma
- `--host 127.0.0.1`: Sadece localhost'tan erişim
- `--port 8000`: Port numarası

### Test Etme

`test_ai.py` scripti ile AI Worker'ı test edebilirsiniz:

```bash
python test_ai.py
```

### Database Reset

Veritabanını sıfırlamak için:

```bash
docker-compose down -v  # Volume'leri sil
docker-compose up -d    # Yeniden başlat
```

### Loglama

FastAPI otomatik log tutar. Detaylı log için:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🔧 Sorun Giderme

### Problem: "Connection refused" hatası

**Çözüm**: PostgreSQL container'ının çalıştığından emin olun:
```bash
docker ps
docker-compose up -d
```

### Problem: "AI Worker bağlantı hatası"

**Çözüm**:
1. Google Colab notebook'unda Cell 7'nin çalıştığını kontrol edin
2. Cloudflare URL'inin güncel olduğunu doğrulayın
3. Colab session'ının aktif olduğundan emin olun

### Problem: "Email already registered"

**Çözüm**: Farklı bir email kullanın veya database'i reset edin.

### Problem: "File must be .txt"

**Çözüm**: Sadece `.txt` uzantılı dosyalar kabul edilir. Word/PDF dosyalarını metin formatına çevirin.

### Problem: "Text too short (minimum 50 characters)"

**Çözüm**: Dosyanın en az 50 karakter içerdiğinden emin olun.

### Problem: Port 5432 kullanımda

**Çözüm**: PostgreSQL zaten yüklüyse Docker port'unu değiştirin:
```yaml
ports:
  - "5433:5432"  # docker-compose.yml'de
```

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. **Fork** edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. **Pull Request** açın

### Geliştirme Alanları

- [ ] JWT authentication sistemi
- [ ] User session management
- [ ] Frontend interface (React/Vue)
- [ ] Batch processing (çoklu dosya desteği)
- [ ] PDF/Word dosya desteği
- [ ] Soru bankası özelliği
- [ ] Kullanıcı dashboard
- [ ] Admin panel
- [ ] Docker production deployment
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Unit & Integration testleri
- [ ] API rate limiting

---

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.

---

## 📞 İletişim

**Proje Sahibi**: Fatma Aleyna

**GitHub**: [@FatmaAleyna](https://github.com/FatmaAleyna)

**Repository**: [Noto Backend](https://github.com/FatmaAleyna/Noto)

---

## 🙏 Teşekkürler

- **Trendyol** - Türkçe optimize LLM modeli
- **Hugging Face** - Model hosting ve transformers kütüphanesi
- **FastAPI** - Modern web framework
- **Google Colab** - Ücretsiz GPU erişimi
- **Cloudflare** - Secure tunneling çözümü

---

<p align="center">
  <strong>Yapay zeka destekli eğitim için geliştirildi ❤️</strong>
</p>

<p align="center">
  <sub>Eğer bu proje size yardımcı olduysa ⭐ vermeyi unutmayın!</sub>
</p>
