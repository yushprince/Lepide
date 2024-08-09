from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from transformers import pipeline
import os

app = FastAPI()

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Directory to store uploaded files
UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}

@app.post("/summarize/")
async def summarize_file(filename: str):
    file_path = f"{UPLOAD_DIR}/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Read the document content
    with open(file_path, "r") as file:
        content = file.read()

    # Generate the summary
    summary = summarizer(content, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
    return {"summary": summary}

@app.get("/")
async def root():
    return {"message": "Welcome to the Document Summarizer API"}
