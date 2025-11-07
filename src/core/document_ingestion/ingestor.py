from langchain_community.document_loaders import(
    TextLoader,
    PyMuPDFLoader,
    Docx2txtLoader,
    UnstructuredHTMLLoader,
    UnstructuredEPubLoader,
)

SPLITTERS = {
    ".xt": TextLoader,
    "md": TextLoader,
    "docx": Docx2txtLoader,
    "pdf": PyMuPDFLoader,
    "html": UnstructuredHTMLLoader,
    "epub": UnstructuredEPubLoader
}

class Ingestor:
    def load(self, path: str):
        split = path.split(".")[-1]
        try:
            loader = SPLITTERS[split](path)
        except Exception as e:
            raise e
        
        return loader.load()
            
    
