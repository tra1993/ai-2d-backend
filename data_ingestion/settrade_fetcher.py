import requests
import json

def fetch_market_data():
    try:
        # Thai Stock Market API မှ live data ဆွဲယူခြင်း
        response = requests.get("https://api.thaistock2d.com/live")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(json.dumps(fetch_market_data()))
