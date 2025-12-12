# Noto - Otonom Eğitim Asistanı 📚

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?style=for-the-badge&logo=fastapi)
![Hugging Face](https://img.shields.io/badge/LLM-Trendyol%207b-yellow?style=for-the-badge&logo=huggingface)
![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20Microservices-purple?style=for-the-badge)

**Noto**, eğitim materyallerini (ders notları, makaleler, akademik metinler) doğal dil işleme (NLP) teknikleriyle analiz eden; eğitimciler ve öğrenciler için otonom olarak **Sınav Soruları** ve **Kapsamlı Özetler** üreten yeni nesil bir yapay zeka platformudur.

---

## 🏗 Mimari Yaklaşım: Hibrit Mikroservis Mimarisi

Bu projede yüksek GPU maliyetlerini minimize etmek ve veri güvenliğini sağlamak amacıyla kendi tasarladığım **Hibrit Mikroservis Mimarisi** (Hybrid Microservices Architecture) yapısını kullandım.

* **Veri Güvenliği (Local):** Hassas kullanıcı verileri ve iş mantığı yerel sunucularda (On-Premise) işlenir.
* **Yüksek Hesaplama (Cloud):** Yoğun işlem gücü gerektiren LLM (Large Language Model) çıkarımları, güvenli tüneller aracılığıyla bulut tabanlı GPU kümeleri (Google Colab/Cloud) üzerinde gerçekleştirilir.

### 🔄 Sistem Akış Şeması
*(Sistemin hibrit çalışma yapısı)*

```text
+-------------------+       HTTP/JSON       +--------------------------+
| Kullanıcı Arayüzü | <-------------------> | FastAPI Sunucusu (Local) |
+-------------------+                       +--------------------------+
                                                         |
                                                         | (SQL)
                                                         v
                                              +---------------------+
                                              |    PostgreSQL DB    |
                                              +---------------------+
                                                         |
                                                         | (Secure Tunnel)
                                                         v
+-------------------+       Inference       +--------------------------+
|  Trendyol-LLM-7b  | <-------------------> | AI Motoru (Google Colab) |
+-------------------+                       +--------------------------+
🚀 Temel ÖzelliklerOtonom Soru Üretimi: Ders notlarından çoktan seçmeli veya klasik sınav soruları üretir.Akıllı Özetleme: Uzun akademik metinleri analiz ederek kritik noktaları özetler.Türkçe NLP Optimizasyonu: Projenin AI katmanında, Türkçe dili için optimize edilmiş Trendyol-LLM-7b-chat-dpo modelini fine-tune ederek entegre ettim.Maliyet Etkin Çözüm: Pahalı GPU sunucuları yerine dağıtık ve hibrit bir yapı kurarak operasyonel maliyeti %80 oranında düşürdüm.🛠 Teknik AltyapıAlanTeknolojiAçıklamaBackendPython, FastAPIYüksek performanslı asenkron APIAI ModelHugging Face, Trendyol-LLMDoğal Dil İşleme ve Üretken Yapay ZekaInfrastructureDocker, Cloudflare TunnelServis izolasyonu ve güvenli tünellemeDatabasePostgreSQLİlişkisel veri ve kullanıcı yönetimi⚙️ Kurulum ve ÇalıştırmaProjeyi yerel ortamınızda test etmek için:1. Repoyu KlonlayınBashgit clone [https://github.com/FatmaAleyna/Noto.git](https://github.com/FatmaAleyna/Noto.git)
cd Noto
2. Gereksinimleri YükleyinBashpip install -r requirements.txt
3. Backend Servisini BaşlatınBashuvicorn main:app --reload
4. AI Worker BağlantısıNot: AI motoru harici bir GPU üzerinde çalışıyorsa, .env dosyasında AI_SERVICE_URL parametresini tünel adresiyle güncelleyin.
