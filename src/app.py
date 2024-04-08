from fastapi import FastAPI
from models import insert_t
from pydantic import BaseModel
from pred import predict_fasttext
from datetime import datetime

# Define a Pydantic model for request body validation
class Item(BaseModel):
    comment: str

app = FastAPI()
@app.get("/")
def get_api():
    sts = "success"
    msg = "Predictive Modeling for Sentiment Analysis IG"
    res_message = {}
    res_message.setdefault("validation", sts)
    res_message.setdefault("message",msg)
    return res_message

@app.post("/predict/")
def predict(data: dict):
    res_ai = {}
    sts = False
    
    try:
        sts, msg = validation_json(data)
        
        if sts:
            THRESHOLD = 0.5
            created_at = datetime.now()
            nama_model = "models\cyberbullying.bin"
            id_ig = data["id_ig"]
            comment_ig = data["comment_ig"]
            prediction, thresh = predict_fasttext(nama_model, comment_ig, THRESHOLD)
            res_ai.setdefault("Prediction_AI", f"Comment bersifat: {prediction}")
            res_ai.setdefault("Threshold", thresh)
            insert_t([id_ig, comment_ig, prediction, created_at, thresh])
            
    except Exception as e:
        msg = e

    resp = {}
    resp.setdefault("Status", sts)
    resp.setdefault("Msg", msg)
    resp.setdefault("Result_AI", res_ai) 

    return resp

def validation_json(data):
    sts = True
    msg = "Proses AI berhasil"
    if "comment_ig" not in data:
        sts = False
        msg = "Proses Gagal, key comment_ig tidak ditemukan"    
    return sts, msg