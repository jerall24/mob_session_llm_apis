"""
Exercise 1: Simple API Call
Make a basic call to the LLM API and print the response.

GOAL: By the end of this exercise, you'll make your first LLM API call!
"""

# TODO 1: Import the required modules
# Hint: You'll need 'os' for environment variables and 'OpenAI' from the openai package


# TODO 2: Initialize the OpenAI client
# Hint: We're connecting to a LiteLLM Proxy, not directly to OpenAI
# You need to pass two parameters:
#   - api_key: Get it from environment variable "LLM_PROXY_API_KEY"
#   - base_url: Get it from environment variable "LLM_PROXY_BASE_URL"


# TODO 3: Make an API call
# Steps:
#   a) Print a message like "Sending request to LLM..."
#   b) Call client.chat.completions.create() with:
#      - model: "gpt-3.5-turbo"
#      - messages: A list with one dictionary containing:
#        * "role": "user"
#        * "content": "What is an API?"
#   c) Store the result in a variable called 'response'


# TODO 4: Extract and print the response
# The response content is at: response.choices[0].message.content
# Print it nicely with a "Response:" header
