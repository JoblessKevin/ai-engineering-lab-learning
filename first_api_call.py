import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

model = os.environ.get("LLM_MODEL", "claude-sonnet-5")

response = client.messages.create(
    model=model,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Explain a neural network in one sentence."
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Stop reason:", response.stop_reason)