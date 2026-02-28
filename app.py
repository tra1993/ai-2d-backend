from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predict import Predictor
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

# CORS အသေဖွင့်ပေးထားပါတယ်
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = Predictor()

class Req(BaseModel):
    session: str

# ဒီအပိုင်းက Browser မှာ {"status": "..."} ပေါ်စေဖို့ပါ
@app.get("/")
async def root():
    return {"status": "Advantage Core V5.5 is Online", "version": "5.5"}

@app.post("/predict")
async def get_prediction(data: Req):
    try:
        # LIVE API SYNC
        res = requests.get("https://api.thaistock2d.com/live", timeout=10).json()
        live = res.get('live', {})
        curr_set = float(live.get('set', 0))
        curr_val = float(live.get('value', 0))
        
        if curr_set == 0:
            hist = requests.get("https://api.thaistock2d.com/2d_result").json()
            curr_set = float(hist[0].get('set', 0))
            curr_val = float(hist[0].get('value', 0))

        out = predictor.execute(data.session, curr_set, curr_val)
        return {
            "status": "success",
            "prediction": out['prediction'],
            "target_lock": out['target_lock'],
            "confidence": out['confidence'],
            "ai_verdict": out['analysis'],
            "set_index": "{:.2f}".format(curr_set),
            "value": "{:.2f}".format(curr_val)
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
