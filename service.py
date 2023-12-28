from __future__ import annotations
import bentoml
from transformers import pipeline

@bentoml.service(
    resources={"memory": "500MiB"},
    traffic={"timeout": 10},
)
class Summarization:
    model_ref = bentoml.models.get("summarization-model")
    
    def __init__(self) -> None:
        # Load model into pipeline
        self.pipeline = pipeline('summarization', self.model_ref.path)
    
    @bentoml.api
    def summarize(self, text: str) -> str:
        result = self.pipeline(text)
        return result[0]['summary_text']