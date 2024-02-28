from fastapi import FastAPI, HTTPException # Importation des Frameworks nécéssaires (fastpi, uvicorn, sqlite3).
import uvicorn
import requests
import json
from chatbot.chatbot import payload, headers, url, provider

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = ["http://localhost", "http://localhost:8001"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

           

@app.get("/test/{name}")
def test(name):
    return {"Hello": name}


@app.post("/{prompt}")
def Chatbot(prompt):
    payload["text"] = prompt
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    rp = result[provider]
    return rp['generated_text']
    
    


@app.get("/test/{prompt}", description="Test!")
def test(prompt):
    return"Yo"

@app.post("/{prompt}", description="Returns EdenAPI's output")
async def chat(prompt):
    payload["text"] = prompt
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    rp = result[provider]
    return rp['generated_text']
    
@app.on_event("startup")
async def startup_event():
    print("Connexion établie")

if __name__ == "__main__":
    uvicorn.run(app, port=8000) # Lancement de Uvicorn.


## 