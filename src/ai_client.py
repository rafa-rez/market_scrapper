# src/ai_client.py
import config

# --- Implementação para Azure OpenAI ---
def _get_azure_analysis(system_prompt, user_prompt):
    from openai import AzureOpenAI
    creds = config.AI_CONFIG["azure"]
    if not all([creds["api_key"], creds["endpoint"], creds["deployment"]]):
        raise ValueError("Credenciais da Azure não configuradas no .env")
    
    client = AzureOpenAI(
        api_key=creds["api_key"],
        api_version="2024-02-15-preview",
        azure_endpoint=creds["endpoint"]
    )
    response = client.chat.completions.create(
        model=creds["deployment"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# --- Implementação para OpenAI (Padrão) ---
def _get_openai_analysis(system_prompt, user_prompt):
    from openai import OpenAI
    creds = config.AI_CONFIG["openai"]
    if not creds["api_key"]:
        raise ValueError("API Key da OpenAI não configurada no .env")

    client = OpenAI(api_key=creds["api_key"])
    response = client.chat.completions.create(
        model=creds["model"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# --- Implementação para Google Gemini ---
def _get_gemini_analysis(system_prompt, user_prompt):
    import google.generativeai as genai
    creds = config.AI_CONFIG["gemini"]
    if not creds["api_key"]:
        raise ValueError("API Key do Gemini não configurada no .env")
    
    genai.configure(api_key=creds["api_key"])
    model = genai.GenerativeModel(
        model_name=creds["model"],
        system_instruction=system_prompt
    )
    response = model.generate_content(user_prompt)
    return response.text.strip()

# --- Implementação para Anthropic Claude ---
def _get_claude_analysis(system_prompt, user_prompt):
    import anthropic
    creds = config.AI_CONFIG["claude"]
    if not creds["api_key"]:
        raise ValueError("API Key da Anthropic não configurada no .env")

    client = anthropic.Anthropic(api_key=creds["api_key"])
    response = client.messages.create(
        model=creds["model"],
        max_tokens=4096, # Aumentado para acomodar prompts maiores
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.content[0].text.strip()

# --- Implementação para Hugging Face ---
def _get_huggingface_analysis(system_prompt, user_prompt):
    from huggingface_hub import InferenceClient
    creds = config.AI_CONFIG["huggingface"]
    if not creds["api_key"]:
        raise ValueError("API Key da Hugging Face não configurada no .env")

    client = InferenceClient(token=creds["api_key"])
    prompt = f"<s>[INST] {system_prompt}\n\n{user_prompt} [/INST]"
    
    # HuggingFace Inference API tem limites de tempo/payload, pode falhar com prompts muito grandes
    response = client.text_generation(prompt, model=creds["model"], max_new_tokens=2048, temperature=0.7)
    return response.strip()


# --- Roteador Principal ---
PROVIDER_MAP = {
    "azure": _get_azure_analysis,
    "openai": _get_openai_analysis,
    "gemini": _get_gemini_analysis,
    "claude": _get_claude_analysis,
    "huggingface": _get_huggingface_analysis,
}

def get_ai_analysis(system_prompt: str, user_prompt: str) -> str:
    """
    Função principal que seleciona o provedor de IA com base na configuração
    e solicita a análise.
    """
    provider = config.AI_PROVIDER.lower()
    analysis_func = PROVIDER_MAP.get(provider)

    if not analysis_func:
        raise ValueError(f"Provedor de IA '{provider}' não é suportado.")

    try:
        print(f"Usando o provedor de IA: {provider.capitalize()}")
        return analysis_func(system_prompt, user_prompt)
    except Exception as e:
        return f"Ocorreu um erro ao se comunicar com a API de {provider.capitalize()}: {e}"