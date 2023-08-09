# Quickstart

This quickstart demonstrates how to build a text summarization application with a Transformer model from the Hugging Face Model Hub.

Perform the following steps to run this project.

1. Clone the repository:

   ```bash
   git clone https://github.com/bentoml/quickstart.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the Transformer model.

   ```bash
   python download_model.py
   ```

4. Serve your model as an HTTP server. This starts a local server at [http://0.0.0.0:3000](http://0.0.0.0:3000/), making your model accessible as a web service.
   
   ```bash
   bentoml serve service:svc
   ```

5. Build your Bento. In the BentoML framework, a Bento is a deployable artifact that contains your application's source code, models, configurations, and dependencies.

   ```bash
   bentoml build
   ```

After your Bento is ready, you can push your Bento to [BentoCloud](https://www.bentoml.com/cloud) or containerize it with Docker and deploy it on a variety of platforms.

For more information, see this [quickstart in the BentoML documentation](https://docs.bentoml.org/en/latest/quickstarts/deploy-a-transformer-model-with-bentoml.html).