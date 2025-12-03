import openai 
import os

def list_proxy_models() -> list[str]:

    api_key = os.getenv("LLM_PROXY_API_KEY")
    base_url = os.getenv("LLM_PROXY_BASE_URL")
    if not api_key or not base_url:
        raise RuntimeError("LLM_PROXY_API_KEY and LLM_PROXY_BASE_URL must be set to list proxy models")

    client = openai.OpenAI(api_key=api_key, base_url=base_url)
    try:
        resp = client.models.list()
        models = [getattr(m, "id", None) for m in getattr(resp, "data", [])]
        return [m for m in models if m]
    except Exception as exc:
        print(f"Failed to list models from proxy: {exc}")


if __name__ == "__main__":
    print(f"Available proxy models:\n")
    for model in list_proxy_models():
        print(f"  {model}")