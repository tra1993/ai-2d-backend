import matplotlib.pyplot as plt
import os

def create_trend_chart(data, labels, filename="trend.png"):
    """ခန့်မှန်းချက် Trend များကို ဇယားအဖြစ် ဖန်တီးခြင်း"""
    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o', linestyle='-', color='#38bdf8')
    plt.title("AI Prediction Trend Analysis")
    plt.xlabel("Timeline")
    plt.ylabel("Value")
    
    # Static directory ထဲတွင် သိမ်းဆည်းခြင်း
    path = os.path.join("public", filename)
    plt.savefig(path)
    plt.close()
    return path

if __name__ == "__main__":
    print("Static visualization module ready.")
