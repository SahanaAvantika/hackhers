# backend/app/main.py
# from fastapi import FastAPI, UploadFile, Form
# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# from model.detect import dummy_detect

# # Initialize Firebase
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# firebase_path = os.path.join(BASE_DIR, "firebase", "serviceAccountKey.json")

# cred = credentials.Certificate(firebase_path)
# firebase_admin.initialize_app(cred)

# #cred = credentials.Certificate("../../firebase/firebase.json") //WRONG DIR
# db = firestore.client()

# app = FastAPI()

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)


# @app.post("/upload")
# async def upload(file: UploadFile):
#     file_path = os.path.join(UPLOAD_DIR, file.filename)
#     with open(file_path, "wb") as f:
#         f.write(await file.read())
#     return {"status": "uploaded", "filename": file.filename}


# @app.post("/analyze")
# async def analyze(
#     uid: str = Form(...),         # user ID
#     uploadId: str = Form(...),    # Firestore upload document ID
#     file_name: str = Form(...)    # name of the uploaded file
# ):
#     file_path = os.path.join(UPLOAD_DIR, file_name)

#     # Run detection
#     result = dummy_detect(file_path)

#     # Update Firestore document: users/{uid}/uploads/{uploadId}
#     db.collection("users").document(uid).collection("uploads").document(uploadId).update(result)

#     return {"status": "analyzed", "result": result}


# backend/app/main.py
from fastapi import FastAPI, UploadFile, Form
import firebase_admin
from firebase_admin import credentials, firestore
from model.detect import dummy_detect
import os

# Firebase Initialization
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
firebase_path = os.path.join(BASE_DIR, "firebase", "serviceAccountKey.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_path)
    firebase_admin.initialize_app(cred)  # no storage bucket

db = firestore.client()

app = FastAPI()

# Local Upload Directory
UPLOAD_DIR = os.path.join(BASE_DIR, "backend", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload Endpoint
@app.post("/upload")
async def upload(uid: str = Form(...), file: UploadFile = Form(...)):
    """
    Save video locally and create Firestore document
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Create Firestore document
    upload_ref = db.collection("users").document(uid).collection("uploads").document()
    upload_ref.set({
        "videoUrl": file_path,  # local path instead of Storage URL
        "probability": None,
        "uploadedAt": firestore.SERVER_TIMESTAMP
    })

    return {"status": "uploaded", "uploadId": upload_ref.id, "videoUrl": file_path}

# Analyze Endpoint
@app.post("/analyze")
async def analyze(uid: str = Form(...), uploadId: str = Form(...)):
    """
    Run detection on local video file and update Firestore
    """
    upload_doc = db.collection("users").document(uid).collection("uploads").document(uploadId).get()
    if not upload_doc.exists:
        return {"error": "Upload not found"}

    video_path = upload_doc.to_dict().get("videoUrl")
    if not video_path:
        return {"error": "Video URL missing"}

    # Run detection on local file
    result = dummy_detect(video_path)

    # Update Firestore document
    db.collection("users").document(uid).collection("uploads").document(uploadId).update(result)

    return {"status": "analyzed", "result": result}

# Get Results Endpoint
@app.get("/results/{uid}/{uploadId}")
async def get_results(uid: str, uploadId: str):
    doc = db.collection("users").document(uid).collection("uploads").document(uploadId).get()
    if doc.exists:
        return doc.to_dict()
    return {"error": "Result not found"}
