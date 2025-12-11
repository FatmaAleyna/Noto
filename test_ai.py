import requests
import urllib3  # Uyarıları gizlemek için bunu ekledik

# Güvenlik uyarısını gizle (Terminal kirlenmesin)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. Colab'den aldığın link (Aynısı kalsın)
API_URL = "https://euphemious-skimpily-tawanda.ngrok-free.dev/soru-uret"

# 2. Test metni
test_metni = """
Yapay zeka, bilgisayarların insan gibi düşünmesini sağlayan teknolojidir.
Makine öğrenmesi ve derin öğrenme bu alanın alt dallarıdır.
"""

print(f"📡 İstek şu adrese gönderiliyor: {API_URL}")
print("⏳ Cevap bekleniyor (SSL iptal edildi)...")

try:
    # --- DÜZELTME BURADA ---
    # verify=False parametresi ekledik. Bu, "Sertifikayı kontrol etme" demektir.
    response = requests.post(API_URL, json={"metin": test_metni}, verify=False)

    if response.status_code == 200:
        sonuc = response.json()
        print("\n✅ BAŞARILI! İşte Yapay Zeka'nın Cevabı:\n")
        print(f"🔹 KLASİK SORU: {sonuc['klasik_soru']}")
        print("-" * 30)
        print(f"🔹 TEST SORUSU: {sonuc['test_sorusu']}")
    else:
        print(f"❌ HATA: Sunucu {response.status_code} kodu döndü.")
        print("Detay:", response.text)

except Exception as e:
    print(f"❌ BAĞLANTI HATASI: {e}")