import transformers
import bentoml

model= "sshleifer/distilbart-cnn-12-6"
task = "summarization"
pipeline = transformers.pipeline(task, model=model)

with bentoml.models.create(
    name='summarization-model',
) as model_ref:
    pipeline.save_pretrained(model_ref.path)
    print(f"Model saved: {model_ref}")
