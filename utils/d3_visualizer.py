import json

def format_for_d3_chart(historical_data, predictions):
    """D3.js Interactive Chart အတွက် ဒေတာများကို JSON ပြုလုပ်ခြင်း"""
    chart_data = {
        "history": [
            {"date": d['date'], "value": d['set']} for d in historical_data
        ],
        "forecast": [
            {"date": p['date'], "value": p['pred_set'], "type": "ai_predicted"} for p in predictions
        ]
    }
    
    # ဤ JSON ကို Frontend က API မှတစ်ဆင့် ဆွဲယူလိမ့်မည်
    return json.dumps(chart_data)

if __name__ == "__main__":
    print("D3.js visualizer utility ready.")
