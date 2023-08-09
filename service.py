import bentoml

summarizer_runner = bentoml.models.get("summarization:latest").to_runner()

svc = bentoml.Service(
    name="summarization", runners=[summarizer_runner]
)

@svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
async def summarize(text: str) -> str:
    generated = await summarizer_runner.async_run(text, max_length=3000)
    return generated[0]["summary_text"]