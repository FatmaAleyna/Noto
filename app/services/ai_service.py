import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# YENİ NGOK/CLOUDFLARE LINKINI BURAYA KOY
BASE_AI_URL = "https://formatting-drill-pizza-outstanding.trycloudflare.com"

def generate_questions_from_text(text: str):
    """Soru Üretme İsteği"""
    url = f"{BASE_AI_URL}/soru-uret"
    try:
        response = requests.post(url, json={"metin": text}, verify=False)
        if response.status_code == 200:
            return {"success": True, **response.json()}
        else:
            return {"success": False, "error": f"Hata: {response.status_code}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def generate_summary_from_text(text: str):
    """Özet Üretme İsteği (YENİ)"""
    url = f"{BASE_AI_URL}/ozet-uret"
    try:
        response = requests.post(url, json={"metin": text}, verify=False)
        if response.status_code == 200:
            return {"success": True, **response.json()}
        else:
            return {"success": False, "error": f"Hata: {response.status_code}"}
    except Exception as e:
        return {"success": False, "error": str(e)}