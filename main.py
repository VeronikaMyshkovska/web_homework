from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI()

@app.get("/api/info")
def info():
    secret=os.getenv("SECRET")
    preview=secret[:5]+"****"+secret[-3:]
    return{"secret_preview":preview}
