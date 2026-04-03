# 🏢 Consultor de CNPJ

Aplicação extremamente simples para verificar dados de empresas brasileiras a partir do CNPJ pela base de dados da Receita Federal usando API do BrasilAPI.

---

## 🚀 Como Usar (Versão Pronta)

Se você quer apenas usar o executável:

1. Vá até a seção **[Releases](https://github.com/LucMC36/consultor-cnpj/releases)** à direita desta página.
2. Baixe o arquivo `.exe` da versão mais recente.
3. Execute o programa no seu computador.
   
---

## 🛠️ Para Desenvolvedores (Código Fonte)

### 📁 Estrutura de Pastas
* `/src`: Contém todo o código-fonte original.
* `/assets`: Ícones e imagens utilizadas no projeto.

### 📚 Estrutura de Arquivos
* `main.py`: Lógica do servidor FastAPI e integração com a Brasil API.
* `desktop.py`: Script para inicializar a interface de janela (Desktop).
* `index.html`: Interface visual do usuário.
* `requirements.txt`: Lista de bibliotecas necessárias para o funcionamento.

### 💻 Tecnologias
* **Linguagem:** Python, HTML e CSS
* **Bibliotecas:** fastapi, uvicorn, httpx e pywebview
* **API de Consulta:** BrasilAPI (https://brasilapi.com.br/docs#tag/CNPJ)

### 🔧 Como Rodar o Código

### 1. Clonar o Repositório

```Bash
git clone https://github.com/LucMC36/consultor-cnpj.git
cd consultor-cnpj
```

### 2. Instalar Dependências
#### Criar o ambiente virtual:

```Bash
python -m venv venv
```

#### No Windows:

```Bash
venv\Scripts\activate
```
#### No Linux/Mac:

```Bash
source venv/bin/activate
```
#### Instalar as bibliotecas do python:

```Bash
pip install -r requirements.txt
```

### 3. Executar
Como Aplicativo Desktop:
Este comando iniciará o servidor em segundo plano e abrirá uma janela do Windows com a interface.

```bash
python desktop.py
```

Como Servidor Web:

```bash
uvicorn main:app --reload
```

Acesse em http://127.0.0.1:8000

📝 Licença
Este projeto está sob a licença MIT. Isso significa que você pode usar, copiar e modificar o código livremente. Veja o arquivo LICENSE para mais detalhes.

👤 Autor
Desenvolvido por LucMC36.

Sinta-se à vontade para dar uma ⭐️ no projeto se ele te ajudou!


---
