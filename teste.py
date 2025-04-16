import tkinter as tk
import os
from datetime import datetime

def criar_janela_anotacoes(root):
    """Cria a interface gráfica centralizada para anotações estilo grimório"""
    janela_anotacoes = tk.Toplevel(root)
    janela_anotacoes.title("Grimório de Anotações")
    janela_anotacoes.geometry("1000x800")
    janela_anotacoes.configure(bg="#3E2723")  # Fundo medieval

    # Título centralizado
    tk.Label(
        janela_anotacoes,
        text="Anotações do Grimório",
        font=("Papyrus", 20, "bold"),
        fg="#FFD700",  # Dourado
        bg="#3E2723"
    ).pack(pady=10)

    # Frame para entradas de texto e botões
    frame_inputs = tk.Frame(janela_anotacoes, bg="#5D4037", bd=5, relief="ridge")
    frame_inputs.pack(pady=20, padx=20)

    # Caixa de texto
    text_area = tk.Text(
        frame_inputs,
        font=("Courier", 12),
        bg="#F5E0C3",
        fg="#000000",
        width=70,
        height=20,
        wrap="word",
        insertbackground="#8B0000",
    )
    text_area.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Variáveis para controlar o estado dos botões
    bold_active = tk.BooleanVar(value=False)
    italic_active = tk.BooleanVar(value=False)

    # Função para aplicar estilos dinamicamente
    def aplicar_estilos(evento=None):
        text_area.tag_configure("bold", font=("Courier", 12, "bold"))
        text_area.tag_configure("italic", font=("Courier", 12, "italic"))

        if bold_active.get():
            text_area.tag_add("bold", "insert", "insert+1c")
        if italic_active.get():
            text_area.tag_add("italic", "insert", "insert+1c")

    # Ativar/desativar negrito
    def toggle_bold():
        bold_active.set(not bold_active.get())
        if bold_active.get():
            btn_negrito.config(relief="sunken")  # Indicar botão pressionado
        else:
            btn_negrito.config(relief="raised")

    # Ativar/desativar itálico
    def toggle_italic():
        italic_active.set(not italic_active.get())
        if italic_active.get():
            btn_italico.config(relief="sunken")  # Indicar botão pressionado
        else:
            btn_italico.config(relief="raised")

    # Vincular a digitação para aplicar estilos
    text_area.bind("<KeyPress>", aplicar_estilos)

    # Botões para alternar os estilos
    btn_negrito = tk.Button(
        frame_inputs,
        text="Negrito",
        command=toggle_bold,
        bg="#FFD700",
        fg="black",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#FFEC8B",
    )
    btn_negrito.grid(row=1, column=0, padx=5, pady=10)

    btn_italico = tk.Button(
        frame_inputs,
        text="Itálico",
        command=toggle_italic,
        bg="#FFD700",
        fg="black",
        font=("Garamond", 12, "italic"),
        relief="raised",
        activebackground="#FFEC8B",
    )
    btn_italico.grid(row=1, column=1, padx=5, pady=10)

    # Botão para salvar anotações
    def salvar_anotacao():
        # Criar pasta "paginas" se não existir
        pasta_paginas = os.path.join(os.path.dirname(__file__), "paginas")
        os.makedirs(pasta_paginas, exist_ok=True)

        # Obter título e texto
        titulo = text_area.get("1.0", "1.end").strip()
        texto = text_area.get("1.0", tk.END).strip()

        # Gerar nome do arquivo
        if not titulo:
            titulo = f"pagina_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        else:
            titulo = titulo.replace(" ", "_")
        arquivo_path = os.path.join(pasta_paginas, f"{titulo}.txt")

        # Salvar conteúdo no arquivo
        with open(arquivo_path, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

        # Exibir mensagem de confirmação
        tk.messagebox.showinfo("Salvar Anotação", f"Anotação salva em:\n{arquivo_path}")

    # Botão para salvar
    btn_salvar = tk.Button(
        janela_anotacoes,
        text="Salvar Anotação",
        command=salvar_anotacao,
        bg="#228B22",
        fg="white",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#32CD32",
    )
    btn_salvar.pack(pady=10)

    # Botão para fechar o grimório
    btn_fechar = tk.Button(
        janela_anotacoes,
        text="Fechar Grimório",
        command=janela_anotacoes.destroy,
        bg="#8B0000",
        fg="white",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#A52A2A",
    )
    btn_fechar.pack(pady=10)