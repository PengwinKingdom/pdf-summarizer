from fastapi import FastAPI, UploadFile, File
import os
from fastapi.middleware.cors import CORSMiddleware

from app.pdf_utils import extract_text_pdf
from app.summarizer import generate_summary,extract_key_points

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message":"API working"}

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/upload-pdf")
async def upload_pdf(file:UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error":"Please upload a PDF file"}
    
    file_path = os.path.join(UPLOAD_FOLDER,file.filename)

    with open(file_path,"wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text_pdf(file_path)

    summary = generate_summary(extracted_text)
    key_points = extract_key_points(extracted_text)

    return{
        "message": "PDF uploaded",
        "filename": file.filename,
        "path": file_path,
        "summary": summary,
        "key_points": key_points
    }