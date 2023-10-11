"""
### FASTAPI
To run the FastAPI server: uvicorn Server.http_server:app
To auto reload: uvicorn Server.http_server:app --reload
To set port: uvicorn Server.http_server:app --reload --port <port_number>

### NGROK
1) Install Ngrok https://ngrok.com/download
MacOS: brew install ngrok/ngrok/ngrok
Linux: snap install ngrok
Win: choco install ngrok

2) Add authtoken: ngrok config add-authtoken <token>

3) Start a tunnel: ngrok http <port_number>
"""
from fastapi import FastAPI
import uvicorn

from typing import List, Tuple, Dict

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello"}

@app.post("/")
async def send():
    pass


if __name__ == "__main__":
   uvicorn.run("http_server:app",
               host="127.0.0.1",
               port=5000,
               reload=True)