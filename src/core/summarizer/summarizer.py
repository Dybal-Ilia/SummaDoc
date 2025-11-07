from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name=__name__)

class Summarizer:
    def __init__(self, llm:str = "llama3.1"):
        self.llm = ChatOllama(model=llm)
        system_prompt_template = """
        You are an AI assistant responsible for creating textual summaries. You follow the 'MapReduce' strategy,
        therefore you'll be provided with chunks of texts one by one. You are to make a good summary of each chunk.
        It is very important that chunks are of good quality as then they'll be combined in one large text.
        Also to help you loggically create summaries you are given a list of summaries so far: {summaries}.
        Do not say anything like 'Ok, here's your summary', just summarize given chunks.
        Do not make up any unexisting information.
        Current chunk to summarize: {chunk}"""
        self.prompt = ChatPromptTemplate.from_template(system_prompt_template)
        self.chain = self.prompt | self.llm

    def summarize(self, chunks:list[Document]):
        summaries = []
        for i, chunk in enumerate(chunks):
            response = self.chain.invoke({
                "summaries": summaries,
                "chunk": chunk.page_content
            })
            logger.info(f"Summarized chunk: {i+1}")
            summary = response.content.strip()
            summaries.append(summary)
        return "".join(summaries)

            