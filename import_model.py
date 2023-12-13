import transformers
import bentoml
from bentoml.models import ModelContext

model= "sshleifer/distilbart-cnn-12-6"
task = "summarization"
pipeline = transformers.pipeline(task, model=model)

with bentoml.models.create(
    name='summarization-model',
    metadata={'model_name': model, 'task_name': task},
    context=ModelContext(framework_name="", framework_versions={}),
    signatures={},
) as model_ref:
    pipeline.save_pretrained(model_ref.path)
    print(f"Model saved: {model_ref}")
