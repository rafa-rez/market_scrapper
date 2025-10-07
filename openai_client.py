# openai_client.py
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente Azure OpenAI a partir das variáveis de ambiente
try:
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-15-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
except TypeError:
    print("Erro: As variáveis de ambiente da Azure OpenAI não foram encontradas.")
    print("Certifique-se de que AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT e AZURE_OPENAI_DEPLOYMENT estão no seu arquivo .env")
    exit()


def get_ai_analysis(system_prompt: str, user_prompt: str) -> str:
    """
    Envia um prompt para o modelo da Azure OpenAI e retorna a análise gerada.

    Args:
        system_prompt: A instrução que define o comportamento do modelo.
        user_prompt: A pergunta ou o contexto a ser analisado.

    Returns:
        A resposta em texto gerada pelo modelo.
    """
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Ocorreu um erro ao se comunicar com a API da OpenAI: {e}"