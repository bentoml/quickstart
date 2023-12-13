from __future__ import annotations
import bentoml
import bentoml_io
from transformers import pipeline

@bentoml_io.service(
    resources={"memory": "500MiB"},
    traffic={"timeout": 1},
)
class Summarization:
    model_ref = bentoml.models.get("summarization-model")
    
    def __init__(self) -> None:
        # Load model into pipeline
        self.pipeline = pipeline(self.model_ref._info.metadata['task_name'], self.model_ref.path)
    
    @bentoml_io.api
    def summarize(self, text: str) -> str:
        result = self.pipeline(text)
        return result[0]['summary_text']