# LLM API Workshop - Python

A hands-on workshop for learning to use LLM APIs with Python, using the OpenAI SDK to connect to a LiteLLM Proxy.

## Prerequisites

- Python 3.7+
- direnv installed ([Installation Guide](https://direnv.net/docs/installation.html))
- make (optional, but recommended for easier setup)

## Quick Start (Using Make)

1. **Copy and configure the environment file:**
   ```bash
   cp .envrc.template .envrc
   ```
   Then edit `.envrc` and replace `your-api-key-here` with your actual API key.

2. **Allow direnv to load the environment:**
   ```bash
   direnv allow
   ```

3. **Run the setup:**
   ```bash
   make setup
   ```

4. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

5. **Run exercises:**
   ```bash
   make run-1    # Exercise 1
   make run-2    # Exercise 2
   make run-3    # Exercise 3
   ```

Run `make help` to see all available commands.

## Manual Setup (Alternative)

If you prefer not to use Make:

1. **Copy and configure the environment file:**
   ```bash
   cp .envrc.template .envrc
   ```
   Then edit `.envrc` and replace `your-api-key-here` with your actual API key.

2. **Allow direnv to load the environment:**
   ```bash
   direnv allow
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Workshop Exercises

The workshop consists of three progressive exercises:

### 1. Simple Call (`1_simple_call.py`)
Make your first API call to ask a simple question.
```bash
make run-1
# or: python 1_simple_call.py
```

### 2. Dynamic Prompt - Madlibs Edition (`2_dynamic_prompt.py`)
Collaborative madlibs activity! Each person contributes a variable to generate a creative story.
```bash
make run-2
# or: python 2_dynamic_prompt.py
```

### 3. Batch Processor - Column Renaming (`3_batch_processor.py`)
Process multiple database column names and get AI-powered renaming suggestions following best practices.
```bash
make run-3
# or: python 3_batch_processor.py
```

## Configuration

- **Base URL:** `https://llm.data.justworks.com`
- **Model:** `gpt-3.5-turbo`
- **Environment Variables:** Set via `.envrc` (loaded by direnv)
  - `LLM_PROXY_API_KEY` - Your API key for the LiteLLM Proxy
  - `LLM_PROXY_BASE_URL` - The base URL for the LiteLLM Proxy

## Notes

- The `.envrc` file is ignored by git to protect your API key
- Results from exercise 3 are saved to `output.json`
- Use `make clean` to remove the virtual environment and generated files
- Use `make help` to see all available Makefile commands
