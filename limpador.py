import os, shutil, requests, json, threading, sys, base64
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

CONFIG_FILE = "config.json"

# --- SEGURANÇA E CONFIGURAÇÃO ---
def ocultar(texto):
    return base64.b64encode(texto.encode()).decode()

def revelar(texto_codificado):
    try: return base64.b64decode(texto_codificado.encode()).decode()
    except: return ""

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            dados = json.load(f)
            return {
                "caminho": dados.get("caminho", ""),
                "token": revelar(dados.get("token", "")),
                "chat_id": revelar(dados.get("chat_id", ""))
            }
    return {"caminho": "", "token": "", "chat_id": ""}

def salvar_config(caminho, token, chat_id):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"caminho": caminho, "token": ocultar(token), "chat_id": ocultar(chat_id)}, f)

# --- FUNÇÃO DE LIMPEZA E ENVIO ---
def enviar_aviso(msg, token, chat_id):
    if not token or not chat_id: return
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
        requests.get(url, timeout=15)
    except: pass

def executar_limpeza():
    conf = carregar_config()
    caminho, token, chat_id = conf["caminho"], conf["token"], conf["chat_id"]
    
    if caminho and os.path.exists(caminho):
        try:
            for item in os.listdir(caminho):
                p = os.path.join(caminho, item)
                try:
                    # Deleta sem passar pela lixeira (evita janelas de confirmação)
                    if os.path.isfile(p) or os.path.islink(p):
                        os.unlink(p)
                    elif os.path.isdir(p):
                        shutil.rmtree(p, ignore_errors=True)
                except: continue 
            
            enviar_aviso(f"🧹 Sucesso! A pasta {caminho} foi limpa hoje.", token, chat_id)
        except Exception as e:
            enviar_aviso(f"❌ Erro na automação: {e}", token, chat_id)
    
    if "--auto" in sys.argv: sys.exit()

# --- INTERFACE MODERNA ---
def criar_icone():
    img = Image.new('RGB', (64, 64), color=(40, 40, 40))
    d = ImageDraw.Draw(img)
    d.ellipse([10, 10, 54, 54], fill=(0, 170, 255))
    return img

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoClean Hutera Pro")
        self.geometry("480x500")
        self.protocol('WM_DELETE_WINDOW', self.minimizar_para_tray)
        
        conf = carregar_config()
        ctk.CTkLabel(self, text="Configuração de Limpeza Diária", font=("Arial", 20, "bold")).pack(pady=20)

        # Campo Pasta
        ctk.CTkLabel(self, text="Pasta alvo:").pack()
        self.ent_path = ctk.CTkEntry(self, width=380)
        self.ent_path.insert(0, conf["caminho"])
        self.ent_path.pack(pady=5)
        ctk.CTkButton(self, text="Selecionar Pasta", command=self.selecionar).pack()

        # Campo Token (com máscara *)
        ctk.CTkLabel(self, text="Bot Token (Telegram):").pack(pady=(20,0))
        self.ent_token = ctk.CTkEntry(self, width=380, show="*")
        self.ent_token.insert(0, conf["token"])
        self.ent_token.pack(pady=5)

        # Campo ID (com máscara *)
        ctk.CTkLabel(self, text="Seu Chat ID:").pack(pady=(15,0))
        self.ent_id = ctk.CTkEntry(self, width=380, show="*")
        self.ent_id.insert(0, conf["chat_id"])
        self.ent_id.pack(pady=5)

        ctk.CTkButton(self, text="SALVAR E TESTAR LIMPEZA", fg_color="green", command=self.salvar_e_testar).pack(pady=30)
        ctk.CTkLabel(self, text="Ao fechar, o app fica oculto no relógio.", font=("Arial", 10)).pack()

    def selecionar(self):
        path = filedialog.askdirectory()
        if path:
            self.ent_path.delete(0, "end")
            self.ent_path.insert(0, path)

    def salvar_e_testar(self):
        salvar_config(self.ent_path.get(), self.ent_token.get(), self.ent_id.get())
        executar_limpeza()
        messagebox.showinfo("Sucesso", "Configurações salvas e limpeza executada!")

    def minimizar_para_tray(self):
        self.withdraw()
        menu = Menu(MenuItem('Abrir Painel', self.mostrar), MenuItem('Sair Totalmente', self.encerrar))
        self.tray = Icon("AutoClean", criar_icone(), "Limpador Ativo", menu)
        threading.Thread(target=self.tray.run, daemon=True).start()

    def mostrar(self):
        if hasattr(self, 'tray'): self.tray.stop()
        self.deiconify()

    def encerrar(self):
        if hasattr(self, 'tray'): self.tray.stop()
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    if "--auto" in sys.argv:
        executar_limpeza()
    else:
        app = App()
        app.mainloop()