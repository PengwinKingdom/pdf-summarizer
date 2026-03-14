# PDF Summarizer

A web backend project for students that allows uploading an academic PDF, extracting its text, and generating a simple summary with key points.

## Features

- Upload a PDF file
- Extract text from the PDF
- Generate a simple summary
- Return key points from the document
- Swagger documentation with FastAPI

## Tech Stack

- Python
- FastAPI
- Uvicorn
- PyPDF

## Project Structure

```bash
pdf-summarizer/
│
├── app/
│   ├── main.py
│   ├── pdf_utils.py
│   └── summarizer.py
│
├── uploads/
├── README.md
└── requirements.txt
```

## Run locally

### Requirements
- Python 3.11+

### 1) Clone
```bash
git clone https://github.com/PengwinKingdom/pdf-summarizer.git
cd pdf-summarizer
```

### 2) Create virtual environment
```bash
python -m venv venv
```

#### For Windows:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```
#### For Mac and Linux:
```bash
source venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the backend
```bash
uvicorn app.main:app --reload
```

Backend URL: http://127.0.0.1:8000

API Docs (Swagger): http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|-------:|----------|-------------|
| GET | / | Check if the API is running |
| GET | /health | Health check |
| POST | /upload-pdf | Upload a PDF, extract text, generate summary and key points |


## Current Status

This is the first MVP version of the project.

At the moment, it can:
- upload a PDF file
- extract text from the PDF
- generate a simple summary
- return key points from the content


