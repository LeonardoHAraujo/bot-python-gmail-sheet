# Bot - Automação de email/planilha

Bot para automação de leitura de emails e alimentação de informações planilha
google sheet.

Este serviço já está implementado e integrado aos serviços do google, tanto sheets
quando ao serviço de email. Para rodar e realizar a automação necessária, basta seguir
os passos abaixo.

Passo a passo:
- Clone este repositório em sua máquina.
- Neste momento você terá apenas os seguintes arquivos.
    - bot.py
    - readme.md
    - .gitignore
    - .env.example
    - requirements.txt
- Renomeie o `.env.example` para `.env` e siga as instruções abaixo.

    ```
    SP='<LINK DA API SPREADSHEET>'
    LOCATION='<TÍTULO DO EMAIL A SER PROCURADO NA SUA CAIXA DE EMAIL>'
    EMAIL='<EMAIL A SER LIDO>'
    PASSWORD_EMAIL='<SENHA CRIADA PARA ESSE EMAIL NO CONSOLE DO GOOGLE>'
    NAME_RANGE='<NOME DA ABA DA PLANILHA QUE SERÁ ESCRITA>'
    SPREADSHEET_ID='<ID DA PLANILHA QUE SERÁ ESCRITA>'
    ```

- Após o preenchimento dos dados necessários, rode o comando abaixo para instalar as dependências do projeto.

    ```
    pip install -r requirements.txt

    Obs: Para rodar este comando, certifique-se que você tenha o python e o pip
    instalados em sua máquina.

    Links para download abaixo:
       - https://www.python.org/downloads/
       - https://phoenixnap.com/kb/install-pip-windows
    ```

- Baixe o arquivo `credentials.json` que o painel da API do google te disponibilizou e coloque na raiz do projeto.
- E por fim rode do comando para executar o bot.

    ```
    python bot.py
    ```

