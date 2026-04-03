import webview
import uvicorn
import threading
import time
import sys
import os
from main import app  

def pegar_caminho_base():
    """Descobre se está rodando como .exe ou script normal"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def iniciar_servidor():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="critical")

if __name__ == '__main__':
    servidor = threading.Thread(target=iniciar_servidor, daemon=True)
    servidor.start()
    time.sleep(1)

    # Resolve o caminho do ícone descompactado pelo PyInstaller
    caminho_base = pegar_caminho_base()
    caminho_icone = os.path.join(caminho_base, 'icone.ico')

    # Cria a janela padrão com o ícone dinâmico
    webview.create_window(
        title='Consulta de CNPJ', 
        url='http://127.0.0.1:8000', 
        maximized=True,
        text_select=True
    )
    
    webview.start(icon=caminho_icone)