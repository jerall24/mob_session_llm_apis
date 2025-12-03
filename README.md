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

## Workshop Structure

This is designed as a **hybrid mob programming session** with three progressive exercises:

### Exercise 1: Simple Call (`1_simple_call.py`) - BUILD IT TOGETHER 🔨
**Format:** Skeleton with TODOs
**Approach:** Mob programming - work through the TODOs as a team

Build your first API call from scratch! The file contains TODO comments guiding you through:
- Importing modules
- Initializing the OpenAI client
- Making an API call
- Printing the response

```bash
python 1_simple_call.py
```

### Exercise 2: Dynamic Prompt - Madlibs Edition (`2_dynamic_prompt.py`) - COLLABORATE 🎨
**Format:** Complete, ready to run
**Approach:** Each person contributes one variable

This is a fun collaborative activity! Each team member fills in one variable (character name, place, object, etc.), then watch the LLM generate a creative story using all your inputs.

```bash
python 2_dynamic_prompt.py
```

### Exercise 3: Batch Processor - Column Renaming (`3_batch_processor.py`) - EXPLORE 🚀
**Format:** Complete solution to discuss
**Approach:** Demo and discussion

See a real-world example of batch processing with LLMs. This shows how to process multiple items in a loop and apply consistent formatting rules. Perfect for sparking ideas about your own use cases!

```bash
python 3_batch_processor.py
```

## Solutions

Complete solutions for all exercises are available in the `solutions/` folder for reference.

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
