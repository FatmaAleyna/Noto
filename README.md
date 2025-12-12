✨ Noto – Otonom Eğitim Asistanı

Eğitim içeriklerini anlayan, özetleyen ve sınav sorularına dönüştüren yapay zekâ platformu.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/FastAPI-High%20Performance-009688?style=for-the-badge&logo=fastapi"> <img src="https://img.shields.io/badge/LLM-Trendyol%207B-yellow?style=for-the-badge&logo=huggingface"> <img src="https://img.shields.io/badge/Architecture-Hybrid%20Microservices-purple?style=for-the-badge"> </p>
🚀 Noto Nedir?

Noto, ders notlarını, makaleleri ve akademik metinleri analiz ederek:

🎯 Otonom sınav soruları üretir

📘 Kapsamlı ve anlamlı özetler çıkarır

🧠 Türkçe diline optimize edilmiş LLM modelleriyle çalışır

⚡ Hibrit mimarisi sayesinde hızlı, güvenli ve düşük maliyetli bir çözüm sunar

Eğitimciler, öğrenciler ve akademik içerik üreten herkes için tasarlanmış yeni nesil bir yapay zeka eğitim asistanıdır.

🏗 Mimari Yapı: Hibrit Mikroservis Mimarisi

Bu projede, veri güvenliği ve maliyet optimizasyonu için özel olarak tasarlanmış Hybrid Microservices Architecture yaklaşımı kullanılmıştır.

🔐 Neden Hibrit?
Bileşen	Konum	Açıklama
API & İş Mantığı	Local (On-Premise)	Kullanıcı verileri ve tüm kritik iş mantığı lokal sunucularda çalışır.
AI–LLM Çalışmaları	Cloud GPU	Ağır hesaplamalar Google Colab/Cloud gibi GPU ortamlarına taşınır.
İletişim	Cloudflare Tunnel	Güvenli ve izole bir bağlantı oluşturur.
🔄 Sistem Akış Diyagramı
+-------------------+       HTTP/JSON       +--------------------------+
| Kullanıcı Arayüzü | <-------------------> | FastAPI Sunucusu (Local) |
+-------------------+                       +--------------------------+
                                                         |
                                                         | SQL
                                                         v
                                              +----------------------+
                                              |    PostgreSQL DB     |
                                              +----------------------+
                                                         |
                                                         | Secure Tunnel
                                                         v
+-------------------+      Inference       +--------------------------+
| Trendyol-LLM-7B   | <-------------------> | AI Worker (Cloud GPU)   |
+-------------------+                       +--------------------------+

⚙️ Özellikler
📝 Otonom Soru Üretimi

Çoktan seçmeli

Klasik/teorik sorular

Bloom taksonomisine uygun zorluk seviyeleri

📚 Akıllı Özetleme

Uzun metinlerden anlam bütünlüğü bozulmadan özet çıkarır.

Temel fikirleri, argümanları ve kritik noktaları yakalar.

🧠 Türkçe NLP İçin Optimize Edilmiş AI

Trendyol-LLM-7b-chat-dpo modeli üzerine fine-tuning yapılmıştır.

Türkçe semantik anlayışı güçlendirilmiştir.

💸 Maliyet Odaklı Tasarım

GPU gerektiren işlemler buluta taşınarak %80 maliyet tasarrufu sağlar.

🛠 Teknik Altyapı
Katman	Teknoloji	Açıklama
Backend	Python, FastAPI	Yüksek performanslı, asenkron API
AI Engine	Hugging Face, Trendyol LLM	Özet ve soru üretim modeli
Veritabanı	PostgreSQL	Kullanıcı & içerik saklama
Altyapı	Docker, Cloudflare Tunnel	Servis izolasyonu ve güvenli bağlantı
Dağıtım	Hybrid Microservices	Lokal API + Cloud GPU Worker
🚀 Kurulum & Çalıştırma
1️⃣ Repoyu Klonlayın
git clone https://github.com/FatmaAleyna/Noto.git
cd Noto

2️⃣ Gereksinimleri Yükleyin
pip install -r requirements.txt

3️⃣ Backend’i Başlatın
uvicorn main:app --reload

4️⃣ AI Worker Bağlantısını Yapılandırın

.env dosyasını açın ve:

AI_SERVICE_URL=https://senin-cloudflare-tunneling-adresin


Cloud GPU üzerinde çalışan AI worker bu URL üzerinden bağlanacaktır.
