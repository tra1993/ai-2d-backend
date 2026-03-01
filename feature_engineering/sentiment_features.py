import numpy as np

def process_sentiment_scores(news_data):
    """သတင်းများမှတစ်ဆင့် ဈေးကွက်၏ စိတ်ခံစားမှုကို feature အဖြစ်ပြောင်းခြင်း"""
    # Positive = 1, Neutral = 0, Negative = -1
    sentiment_map = {"Positive": 1.0, "Neutral": 0.0, "Negative": -1.0}
    
    scores = [sentiment_map.get(n['sentiment'], 0) for n in news_data]
    avg_score = np.mean(scores) if scores else 0
    
    return {
        "market_sentiment_score": avg_score,
        "is_optimistic": 1 if avg_score > 0.2 else 0
    }

if __name__ == "__main__":
    print("Sentiment feature engineering module is operational.")
