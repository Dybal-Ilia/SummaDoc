from llama_cloud_services import LlamaParse
from src.core.utils import logger
from dotenv import load_dotenv
import os

load_dotenv()

LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

class Ingestor:
    def __init__(self):
        self.parser = LlamaParse(
            api_key=LLAMA_CLOUD_API_KEY,
            verbose=True,
            parse_mode="parse_page_with_llm"
        )
    
    
    async def ingest(self, path:str):
        try:
            documents = await self.parser.aparse(path)
            markdwon_documents = documents.get_markdown_documents()
            logger.info("Document parsed successfully")
            return markdwon_documents
        except FileNotFoundError:
            logger.error("Seems like {path} does not exist")
            return []
        except Exception as e:
            logger.error(f"An error occured while parsing document: {str(e)}")
            return []


