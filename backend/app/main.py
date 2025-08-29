# backend/main.py
from fastapi import FastAPI, UploadFile, Form
import firebase_admin
from firebase_admin import credentials, firestore
import os
from model.detect import dummy_detect

# Initialize Firebase
cred = credentials.Certificate("../firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"status": "uploaded", "filename": file.filename}

@app.post("/analyze")
async def analyze(file_name: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    result = dummy_detect(file_path)
    db.collection("results").document(file_name).set(result)
    return result

@app.get("/results/{file_name}")
async def get_results(file_name: str):
    doc = db.collection("results").document(file_name).get()
    if doc.exists:
        return doc.to_dict()
    return {"error": "Result not found"}
