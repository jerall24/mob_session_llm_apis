"""
Exercise 1: Simple API Call
Make a basic call to the LLM API and print the response.
"""

import os
from openai import OpenAI

# Initialize the OpenAI client
# We're connecting to a LiteLLM Proxy, not directly to OpenAI
client = OpenAI(
    api_key=os.environ.get("LLM_PROXY_API_KEY"),
    base_url=os.environ.get("LLM_PROXY_BASE_URL")
)

# Make a simple API call
print("Sending request to LLM...")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is an API?"}
    ]
)

# Extract and print the response content
answer = response.choices[0].message.content
print("\nResponse:")
print(answer)
