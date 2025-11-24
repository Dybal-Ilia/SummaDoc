from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.core.utils import logger
class Splitter:
    def __init__(self, max_chunk_size: int = 2000, chunk_overlap: int = 300):
        self.splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""],
    )

    def split(self, documents):
        chunks = []
        for doc in documents:
            chunks.extend(self.splitter.split_text(doc.text))
        logger.info(f"Total {len(chunks)} created")
        return chunks