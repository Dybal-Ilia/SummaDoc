from transformers import BartTokenizer, BartForConditionalGeneration
import torch
from src.core.utils import logger

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer:BartTokenizer = BartTokenizer.from_pretrained(model_name)
        self.model:BartForConditionalGeneration = BartForConditionalGeneration.from_pretrained(model_name).to(self.device)
        logger.info(f"Model is set to device: {self.device}")
        
    async def summarize(self, chunks: list) -> str:
        """
        Takes a list of Document chunks, summarizes each one, 
        and joins them into a coherent bulleted list.
        """
        summaries = []
        for i, chunk in enumerate(chunks):
            logger.info(f"Summarizing chunk {i} / {len(chunks)}")
            inputs = self.tokenizer(
                chunk,
                truncation=True,
                max_length=1000,
                return_tensors="pt"
            ).to(self.device)

            summary_ids = self.model.generate(
                **inputs,
                max_length=600,
                min_length=300,
                num_beams=4,
                length_penalty=2.0,
                early_stopping=True,
            )
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            logger.info(f"Successfully generated summary for chunk {i} / {len(chunks)}")
            summaries.append(summary)
        
        pre_summary = "\n".join(summaries)
        inputs = self.tokenizer(
            pre_summary,
            truncation=True,
            max_length=1000,
            return_tensors="pt",
        ).to(self.device)
        logger.info("Starting final summarization")
        summary_ids = self.model.generate(
            **inputs,
            max_length=1024,
            min_length=600,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True,
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary