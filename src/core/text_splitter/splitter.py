from langchain_text_splitters import RecursiveCharacterTextSplitter

class Splitter:
    def __init__(self, max_chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=max_chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, documnets):
        return self.text_splitter.split_documents(documents=documnets)