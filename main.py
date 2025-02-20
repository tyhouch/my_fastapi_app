from fastapi import FastAPI
import anthropic
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/simple_generate")
def simple_generate():
    """
    Calls the Anthropic Claude 3.5 Sonnet model and returns the response.
    Make sure you have an environment variable named ANTHROPIC_API_KEY set, e.g.:
    export ANTHROPIC_API_KEY="YOUR_API_KEY"
    """
    # Initialize the Anthropic client. Assumes ANTHROPIC_API_KEY is set in your environment.
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Why is the ocean salty?"
                    }
                ]
            }
        ]
    )
    return {"poem": message.content}
