# Noto: Hibrit Mimari ile Güçlendirilmiş Otonom Sınav ve Özet Üretim Sistemi

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688)
![Docker](https://img.shields.io/badge/Docker-PostgreSQL-2496ED)
![AI Model](https://img.shields.io/badge/AI-Trendyol%20LLM%207B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Proje Hakkında

**Noto**, eğitim materyallerini (ders notları, makaleler, akademik metinler) doğal dil işleme (NLP) teknikleriyle analiz eden; eğitimciler ve öğrenciler için otonom olarak **Sınav Soruları** ve **Kapsamlı Özetler** üreten yeni nesil bir yapay zeka platformudur.

Bu proje, yüksek donanım maliyetlerini minimize etmek ve veri güvenliğini sağlamak amacıyla **Hibrit Mikroservis Mimarisi (Hybrid Microservices Architecture)** üzerine inşa edilmiştir. Hassas kullanıcı verileri ve iş mantığı yerel sunucularda (On-Premise) işlenirken, yoğun hesaplama gücü gerektiren LLM (Large Language Model) çıkarımları, güvenli tüneller aracılığıyla bulut tabanlı GPU kümeleri üzerinde gerçekleştirilir.

---

## 🏗️ Teknik Mimari ve Çalışma Prensibi

Noto, kaynak verimliliğini maksimize etmek için dağıtık bir sistem tasarımına sahiptir:

```mermaid
graph LR
    Client[Kullanıcı Arayüzü] -->|HTTP/JSON| Backend[FastAPI Sunucusu (Local)]
    Backend -->|SQL| DB[(PostgreSQL / Docker)]
    Backend -->|Secure Tunnel (Cloudflare)| AI_Worker[AI Motoru (Google Colab A100)]
    AI_Worker -->|Inference| Model[Trendyol-LLM-7b]
    Model -->|Generated Text| AI_Worker
    AI_Worker -->|Response| Backend

🧠 Yapay Zeka Metodolojisi
Projenin AI katmanında, Türkçe dili için optimize edilmiş Trendyol-LLM-7b-chat-dpo modeli kullanılmaktadır. Modelin başarımı, projeye özgü geliştirilen "Prompt Engineering V7" mimarisi ile artırılmıştır:

-Few-Shot Learning (Az Örnekle Öğrenme): Modele sadece talimat verilmez; ideal soru ve özet yapıları bağlam (context) içerisinde örneklenerek çıktının akademik standartlara uyması sağlanır.
-Chain-of-Thought (Düşünce Zinciri): Karmaşık metinlerde modelin adım adım analiz yapması sağlanarak halüsinasyon (yanlış bilgi üretimi) oranı minimize edilmiştir.
-Context Window Optimization: Uzun akademik metinler, anlamsal bütünlüğü bozmayacak şekilde parçalanarak (chunking) işlenir.

🎯 Temel Özellikler
1. Otonom Soru Üretimi
Klasik (Açık Uçlu) Sorular: Bloom Taksonomisi'nin analiz ve değerlendirme basamaklarına uygun, kavramsal derinliği olan sorular üretir.
Çoktan Seçmeli (Test) Sorular: Çeldiricileri (yanlış şıklar) metindeki kavramlarla ilişkili ancak mantıksal olarak yanlış kurgulanmış, yüksek ayırt ediciliğe sahip 5 şıklı sorular oluşturur.

2. Akıllı Akademik Özetleme
Metindeki teknik terminolojiyi (örn: Polymorphism, Hash, Latency) koruyarak, metnin özünü kaybetmeden Türkçe özetleme yapar.
Yüzeysel bir kısaltma yerine, metindeki süreçleri ve neden-sonuç ilişkilerini bağlayan detaylı bir sentez sunar.

3. Dosya Tabanlı İşleme
Kullanıcıların .txt formatındaki ham ders notlarını sisteme yüklemesine ve bu dosyalar üzerinden işlem yapmasına olanak tanır.

4. Güvenlik ve Veri Yönetimi
Argon2 Hashing: Kullanıcı parolaları askeri düzeyde şifreleme ile saklanır.
Dockerize Veritabanı: Tüm veriler izole edilmiş PostgreSQL konteynerlerinde tutulur.

Katman	        Teknoloji	                Açıklama
Backend	        Python 3.11, FastAPI	    Yüksek performanslı asenkron API sunucusu.
Veritabanı	    PostgreSQL 15, SQLAlchemy	İlişkisel veri modelleme ve ORM yapısı.
DevOps	        Docker, Docker Compose	    Konteynerizasyon ve servis orkestrasyonu.
AI Model	    Trendyol-LLM-7b	            Türkçe DPO (Direct Preference Optimization) ile eğitilmiş model.
AI Tools	    HuggingFace, BitsAndBytes	Model optimizasyonu ve 4-bit quantization.
Tunneling	    Cloudflare Tunnel	        Localhost ve Cloud arasındaki güvenli köprü.


Kurulum ve Çalıştırma
Projeyi yerel ortamınızda ayağa kaldırmak için aşağıdaki adımları izleyin.

Gereksinimler
Python 3.10 veya üzeri
Docker Desktop

Adım 1: Depoyu Klonlayın
git clone [https://github.com/FatmaAleyna/noto-backend.git]
cd noto-backend

Adım 2: Sanal Ortamı Hazırlayın
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

Adım 3: Bağımlılıkları Yükleyin
pip install -r requirements.txt

Adım 4: Veritabanını Başlatın (Docker)
docker-compose up -d

Adım 5: Backend Sunucusunu Başlatın
uvicorn main:app --reload

**Sunucu adresi: http://127.0.0.1:8000**

Adım 6: AI Servisini Bağlayın (Google Colab)
Noto_AI_Worker.ipynb dosyasını Google Colab'de açın.

Çalışma zamanı türünü T4 GPU veya A100 GPU olarak seçin.

Tüm hücreleri çalıştırın.

Çıktı olarak verilen Cloudflare Linkini kopyalayın.

Projedeki app/services/ai_service.py dosyasındaki BASE_AI_URL değişkenini bu link ile güncelleyin.

📚 API Dokümantasyonu
Sistem çalıştığında Swagger UI üzerinden interaktif testler yapabilirsiniz: 👉 https://www.google.com/search?q=http://127.0.0.1:8000/docs

Ana Endpoint'ler
POST /users/register - Yeni kullanıcı kaydı.
POST /questions/generate-from-file - Yüklenen dosyadan soru seti üretir.
POST /summary/generate-from-file - Yüklenen dosyanın akademik özetini çıkarır.
