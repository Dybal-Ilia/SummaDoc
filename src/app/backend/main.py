from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pathlib import Path
import shutil
import time
import asyncio
from src.core.document_ingestion.ingestor import Ingestor
from src.core.text_splitter.splitter import Splitter
from src.core.summarizer.summarizer import Summarizer

app = FastAPI(title="SummaDoc")

UPLOAD_DIR = Path("src/uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ingestor = Ingestor()
splitter = Splitter(max_chunk_size=2048, chunk_overlap=50)
summarizer = Summarizer()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    documents = ingestor.load(str(file_path))
    chunks = splitter.split(documents)
    summary = summarizer.summarize(chunks)

    return {"filename": file.filename,
            "summary": summary}
