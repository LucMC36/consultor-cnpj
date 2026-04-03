import sys
import os
import re
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# Configuração de CORS (boa prática para garantir que o front-end se comunique sem bloqueios)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 1. Função auxiliar para o PyInstaller ---
def pegar_caminho_base():
    """
    Retorna o caminho absoluto do projeto.
    Se estiver rodando como .exe (compilado), usa a pasta temporária do sistema.
    Caso contrário, usa a pasta do próprio script.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

# --- 2. Rota para servir o Front-end (HTML) ---
@app.get("/")
async def servir_frontend():
    caminho_base = pegar_caminho_base()
    caminho_html = os.path.join(caminho_base, 'index.html')
    
    if not os.path.exists(caminho_html):
        raise HTTPException(status_code=404, detail="Arquivo index.html não encontrado.")
        
    return FileResponse(caminho_html)

# --- 3. Rota da API (Back-end) para consultar o CNPJ ---
@app.get("/api/cnpj/{cnpj}")
async def consultar_cnpj(cnpj: str):
    # Remove qualquer caractere que não seja número por segurança
    cnpj_limpo = re.sub(r'\D', '', cnpj)
    
    if len(cnpj_limpo) != 14:
        raise HTTPException(status_code=400, detail="CNPJ deve conter 14 dígitos válidos.")

    url_brasil_api = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    
    # Faz a requisição assíncrona para a Brasil API
    async with httpx.AsyncClient() as client:
        response = await client.get(url_brasil_api)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="CNPJ não encontrado ou erro na API externa.")

    dados_brutos = response.json()

    # Formatação do endereço
    endereco_formatado = f"{dados_brutos.get('descricao_tipo_de_logradouro', '')} {dados_brutos.get('logradouro', '')}, {dados_brutos.get('numero', 'S/N')} - {dados_brutos.get('bairro', '')}, {dados_brutos.get('cep', '')}, {dados_brutos.get('municipio', '')}/{dados_brutos.get('uf', '')}"

    dados_filtrados = {
        "razao_social": dados_brutos.get("razao_social", "Não informada"),
        "nome_fantasia": dados_brutos.get("nome_fantasia") or dados_brutos.get("razao_social", "Não informada"),
        "CNPJ": dados_brutos.get("cnpj"),
        "endereco_completo": endereco_formatado,
        "situacao_cadastral": dados_brutos.get("descricao_situacao_cadastral", "Desconhecida")
        
    }

    return dados_filtrados