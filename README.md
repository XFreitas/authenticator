# Autenticador TOTP em Linha de Comando

Este projeto é uma ferramenta de linha de comando (CLI) para gerar e exibir códigos de autenticação de dois fatores (TOTP), similar ao Google Authenticator, diretamente no seu terminal.

A aplicação mostra o código atual e uma barra de progresso que indica o tempo restante até que o código seja atualizado.

![Screenshot](https://i.imgur.com/example.png)  <!-- Você pode substituir por um screenshot real -->

## Funcionalidades

- Gera códigos TOTP baseados em um segredo.
- Exibe o código atual e o tempo de expiração em tempo real.
- Interface de terminal rica e amigável, utilizando a biblioteca `rich`.
- Copia o código gerado para a área de transferência automaticamente (funcionalidade a ser implementada).

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd autenticador
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O projeto usa `setuptools`. Para instalar as dependências e o próprio projeto em modo editável, execute:
    ```bash
    pip install -e .
    ```

## Configuração

Antes de executar a aplicação, você precisa configurar sua chave secreta TOTP.

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Dentro do arquivo `.env`, adicione sua chave secreta no seguinte formato:

    ```
    SECRET_HCPA="SUA_CHAVE_SECRETA_AQUI"
    ```
    Substitua `"SUA_CHAVE_SECRETA_AQUI"` pela chave fornecida pelo serviço para o qual você está gerando o código (por exemplo, Redmine, Google, etc.).

## Como Usar

Após a instalação e configuração, você pode executar a aplicação de duas maneiras:

1.  **Executando o script principal:**
    ```bash
    python main.py
    ```

2.  **Usando o ponto de entrada do console script (recomendado):**
    Como o projeto foi instalado com `pip install -e .`, um comando foi criado no seu ambiente virtual. Basta executar:
    ```bash
    autenticador_redmine
    ```

Para fechar a aplicação, pressione `Ctrl+C`.

## Dependências Principais

- [rich](https://github.com/Textualize/rich): Para a criação de interfaces de linha de comando ricas e bonitas.
- [pyotp](https://github.com/pyauth/pyotp): Para a geração dos códigos TOTP.
- [python-dotenv](https://github.com/theskumar/python-dotenv): Para carregar variáveis de ambiente a partir de um arquivo `.env`.
