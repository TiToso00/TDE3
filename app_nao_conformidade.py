import tkinter as tk
from tkinter import messagebox

# Função para registrar a não-conformidade
def registrar_nao_conformidade():
    titulo = titulo_entry.get()
    descricao = descricao_entry.get("1.0", tk.END)
    responsavel = responsavel_entry.get()
    status = status_var.get()

    if titulo and descricao.strip() and responsavel:
        # Salvar em arquivo .txt
        with open("nao_conformidades.txt", "a") as file:
            file.write(f"Título: {titulo}\n")
            file.write(f"Descrição: {descricao.strip()}\n")
            file.write(f"Responsável: {responsavel}\n")
            file.write(f"Status: {status}\n")
            file.write("-" * 40 + "\n")
        messagebox.showinfo("Sucesso", "Não-conformidade registrada com sucesso!")
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Função para limpar os campos
def limpar_campos():
    titulo_entry.delete(0, tk.END)
    descricao_entry.delete("1.0", tk.END)
    responsavel_entry.delete(0, tk.END)
    status_var.set("Aberto")

# Função para visualizar as não-conformidades
def visualizar_nao_conformidades():
    try:
        with open("nao_conformidades.txt", "r") as file:
            conteudo = file.read()
        messagebox.showinfo("Não-Conformidades Registradas", conteudo)
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Nenhuma não-conformidade registrada ainda.")

# Configuração da janela principal
root = tk.Tk()
root.title("Registro de Não-Conformidades")
root.geometry("400x400")

# Rótulos e entradas
tk.Label(root, text="Título:").pack(pady=5)
titulo_entry = tk.Entry(root, width=40)
titulo_entry.pack(pady=5)

tk.Label(root, text="Descrição:").pack(pady=5)
descricao_entry = tk.Text(root, width=40, height=5)
descricao_entry.pack(pady=5)

tk.Label(root, text="Responsável:").pack(pady=5)
responsavel_entry = tk.Entry(root, width=40)
responsavel_entry.pack(pady=5)

tk.Label(root, text="Status:").pack(pady=5)
status_var = tk.StringVar(value="Aberto")
tk.OptionMenu(root, status_var, "Aberto", "Em Progresso", "Fechado").pack(pady=5)

# Botões
tk.Button(root, text="Registrar", command=registrar_nao_conformidade).pack(pady=10)
tk.Button(root, text="Visualizar Não-Conformidades", command=visualizar_nao_conformidades).pack(pady=10)

# Iniciar a aplicação
root.mainloop()
