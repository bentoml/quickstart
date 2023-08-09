import transformers
import bentoml

model= "sshleifer/distilbart-cnn-12-6"
task = "summarization"

bentoml.transformers.save_model(
    task,
    transformers.pipeline(task, model=model),
    metadata=dict(model_name=model),
)