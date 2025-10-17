# backend/services/data_ingestion.py
import requests
from backend.core.config import settings

def test_api(symbol="AAPL"):
    api_key = settings.FINNHUB_API_KEY  # make sure your .env has FINNHUB_API_KEY
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"

    print("Requesting URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()  # will raise error for bad response
        data = response.json()
        print("API connected successfully! Sample data:", data)
    except Exception as e:
        print("API connection failed:", e)

if __name__ == "__main__":
    test_api("AAPL")  # you can change the symbol
