import requests

def fetch_latest_news():
    """Settrade နှင့် သတင်းဌာနများမှ စီးပွားရေးသတင်းများကို ရယူခြင်း"""
    print("📰 Fetching market news for sentiment analysis...")
    # FinGPT အတွက် သတင်းစာသားများ စုဆောင်းခြင်း
    news_samples = [
        {"source": "Settrade", "text": "SET Index shows strong recovery in morning session."},
        {"source": "FinanceNews", "text": "Global markets react to new economic policies."}
    ]
    return news_samples

if __name__ == "__main__":
    news = fetch_latest_news()
    print(f"Fetched {len(news)} news headlines.")
