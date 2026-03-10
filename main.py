# main.py
#uvicorn main:app --reload
from fastapi import FastAPI
from pydantic import BaseModel


class Soru(BaseModel):
    metin:str
    sicaklik:float


app = FastAPI()
@app.get("/")
def main():
    return {"mesaj":"Merhaba"}

@app.get("/selam/{isim}")

def selamlama(isim : str):
    return{"mesaj":f"Merhaba {isim}, ilk api'ıma hoş geldin"}

@app.get("/topla/{x}/{y}")
def toplama(x:int,y:int):
    return {"sonuc":x+y}


@app.post("/analiz")
def analiz(veri:Soru):
    if "AI" in veri.metin:
        return {"sonuc":"AI"}
    else:
        return {"sonuc":"AI yok"}