# 🧹 AutoClean Hutera Pro

O **AutoClean Hutera Pro** é uma ferramenta de automação para limpeza de arquivos e pastas, desenvolvida em Python. O sistema é ideal para manter servidores ou máquinas locais organizadas, deletando arquivos temporários ou logs diariamente e notificando o usuário via Telegram.

---

## ⚙️ Como o Sistema Funciona

O software possui dois modos de operação:
1.  **Interface Gráfica (GUI):** Onde você configura a pasta alvo, seu Bot Token e seu Chat ID.
2.  **Modo Silencioso (`--auto`):** Usado pelo Agendador de Tarefas do Windows para executar a limpeza em segundo plano, sem abrir janelas, e enviar o relatório para o seu celular.

---

## 🚀 Passo a Passo para Configuração

### 1. Preparando o Telegram (Token e ID)
Para receber as notificações, você precisa de um bot próprio:
1.  No Telegram, procure pelo **@BotFather** e envie `/newbot`.
2.  Siga as instruções para dar um nome ao bot e guarde o **API TOKEN** gerado.
3.  Procure pelo bot **@userinfobot** e clique em "Começar" para obter seu **Chat ID** (um número de 9 ou 10 dígitos).
4.  **Importante:** Envie uma mensagem inicial ("Oi") para o seu bot recém-criado para autorizá-lo a te enviar mensagens.

### 2. Gerando o Executável (.exe)
Se você baixou o código-fonte e deseja gerar seu próprio executável:
1.  Instale as bibliotecas necessárias:
    ```bash
    pip install customtkinter requests pystray pillow pyinstaller
    ```
2.  Gere o executável com o comando:
    ```bash
    python -m PyInstaller --noconsole --onefile limpador.py
    ```
3.  O arquivo pronto estará na pasta `dist/`.

### 3. Configurando o Agendador de Tarefas do Windows
Para que a limpeza seja automática:
1.  Abra o **Agendador de Tarefas** e clique em **Criar Tarefa Básica**.
2.  Escolha a frequência (ex: Diariamente) e o horário.
3.  Em **Ação**, escolha "Iniciar um programa" e selecione o `limpador.exe`.
4.  No campo **Adicionar argumentos**, digite exatamente: `--auto`.
5.  No campo **Iniciar em**, coloque o caminho da pasta onde o executável está.
6.  Nas propriedades da tarefa, marque "Despertar o computador para executar esta tarefa".

---

## 🔒 Segurança e Privacidade
* **Campos Mascarados:** O Token e o ID aparecem como `***` na interface para evitar exposição.
* **Ofuscação local:** As credenciais são salvas no arquivo `config.json` de forma codificada (Base64), impedindo a leitura simples por terceiros.
* **Exclusão Direta:** O sistema utiliza `os.unlink` e `shutil.rmtree`, deletando arquivos permanentemente sem passar pela lixeira, evitando avisos de confirmação do Windows.

---

## 🛠️ Tecnologias Utilizadas
* Python 3.10+
* CustomTkinter (Interface Moderna)
* Pystray (Ícone na Bandeja do Sistema)
* API de Bots do Telegram

---

# 🧹 AutoClean Hutera Pro (English Version)

**AutoClean Hutera Pro** is a directory cleaning automation tool developed in Python. It is ideal for keeping servers or local machines organized by deleting temporary files or logs daily and notifying the user via Telegram.

---

## ⚙️ How it Works

The software features two operating modes:
1.  **Graphical User Interface (GUI):** Where you configure the target folder, your Bot Token, and your Chat ID.
2.  **Silent Mode (`--auto`):** Used by the Windows Task Scheduler to perform cleaning in the background without opening windows and sending the report to your phone.

---

## 🚀 Step-by-Step Configuration

### 1. Preparing Telegram (Token and ID)
To receive notifications, you need your own bot:
1.  On Telegram, search for **@BotFather** and send `/newbot`.
2.  Follow the instructions to name the bot and save the **API TOKEN** generated.
3.  Search for the bot **@userinfobot** and click "Start" to obtain your **Chat ID** (a 9 or 10-digit number).
4.  **Important:** Send an initial message ("Hi") to your newly created bot to authorize it to send you messages.

### 2. Generating the Executable (.exe)
If you downloaded the source code and want to generate your own executable:
1.  Install the required libraries:
    ```bash
    pip install customtkinter requests pystray pillow pyinstaller
    ```
2.  Generate the executable with the command:
    ```bash
    python -m PyInstaller --noconsole --onefile limpador.py
    ```
3.  The ready-to-use file will be in the `dist/` folder.

### 3. Setting up Windows Task Scheduler
To make the cleaning automatic:
1.  Open **Task Scheduler** and click **Create Basic Task**.
2.  Choose the frequency (e.g., Daily) and the time.
3.  In **Action**, choose "Start a program" and select `limpador.exe`.
4.  In the **Add arguments** field, type exactly: `--auto`.
5.  In the **Start in** field, enter the path to the folder where the executable is located.
6.  In the task properties, check "Wake the computer to run this task".

---

## 🔒 Security and Privacy
* **Masked Fields:** Token and ID appear as `***` in the interface to prevent exposure.
* **Local Obfuscation:** Credentials are saved in the `config.json` file in an encoded format (Base64), preventing simple reading by third parties.
* **Direct Deletion:** The system uses `os.unlink` and `shutil.rmtree`, deleting files permanently without going through the recycle bin, avoiding Windows confirmation prompts.

---

## 🛠️ Technologies Used
* Python 3.10+
* CustomTkinter (Modern Interface)
* Pystray (System Tray Icon)
* Telegram Bot API