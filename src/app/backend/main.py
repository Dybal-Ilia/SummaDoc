from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil
from src.core.document_ingestion.ingestor import Ingestor
from src.core.text_splitter.splitter import Splitter
from src.core.summarizer.summarizer import Summarizer

app = FastAPI(title="SummaDoc")

UPLOAD_DIR = Path("src/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ingestor = Ingestor()
splitter = Splitter()
summarizer = Summarizer()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        documents = await ingestor.ingest(str(file_path))
        chunks = splitter.split(documents)
        summary = await summarizer.summarize(chunks)
    finally:
        file.file.close()
        file_path.unlink(missing_ok=True)

    return {"filename": file.filename, "summary": summary}

