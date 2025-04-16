import tkinter as tk
from tkinter import messagebox
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
        fg="#FFD700",
        bg="#3E2723"
    ).pack(pady=10)

    # Frame centralizado com conteúdo
    frame_inputs = tk.Frame(janela_anotacoes, bg="#5D4037", bd=5, relief="ridge")
    frame_inputs.pack(pady=20, padx=20)

    # Entrada de título
    tk.Label(
        frame_inputs,
        text="Título:",
        font=("Garamond", 14, "bold"),
        fg="#FFFFFF",
        bg="#5D4037"
    ).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_titulo = tk.Entry(
        frame_inputs,
        font=("Garamond", 14),
        bg="#F5E0C3",
        fg="#000000",
        width=50
    )
    entry_titulo.grid(row=0, column=1, padx=5, pady=5)

    # Caixa de texto
    tk.Label(
        frame_inputs,
        text="Texto:",
        font=("Garamond", 14, "bold"),
        fg="#FFFFFF",
        bg="#5D4037"
    ).grid(row=1, column=0, sticky="ne", padx=5, pady=5)
    text_area = tk.Text(
        frame_inputs,
        font=("Courier", 12),
        bg="#F5E0C3",
        fg="#000000",
        width=70,
        height=20,
        wrap="word",
        insertbackground="#8B0000"
    )
    text_area.grid(row=1, column=1, padx=5, pady=5)

    # Scrollbar
    scrollbar = tk.Scrollbar(frame_inputs, command=text_area.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")
    text_area.config(yscrollcommand=scrollbar.set)

    # Configurar estilos
    text_area.tag_configure("bold", font=("Courier", 12, "bold"))
    text_area.tag_configure("italic", font=("Courier", 12, "italic"))

    def aplicar_formatacao(tag):
        try:
            start = text_area.index("sel.first")
            end = text_area.index("sel.last")
            if tag in text_area.tag_names("sel.first"):
                text_area.tag_remove(tag, start, end)
            else:
                text_area.tag_add(tag, start, end)
        except tk.TclError:
            messagebox.showwarning("Formatação", "Selecione um trecho de texto para aplicar a formatação.")

    # Botões de formatação
    frame_formatacao = tk.Frame(frame_inputs, bg="#5D4037")
    frame_formatacao.grid(row=2, column=1, pady=10)

    btn_negrito = tk.Button(
        frame_formatacao,
        text="Negrito",
        command=lambda: aplicar_formatacao("bold"),
        bg="#FFD700",
        fg="black",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#FFEC8B"
    )
    btn_negrito.pack(side="left", padx=10)

    btn_italico = tk.Button(
        frame_formatacao,
        text="Itálico",
        command=lambda: aplicar_formatacao("italic"),
        bg="#FFD700",
        fg="black",
        font=("Garamond", 12, "italic"),
        relief="raised",
        activebackground="#FFEC8B"
    )
    btn_italico.pack(side="left", padx=10)

    # Botão de salvar
    def salvar_anotacao():
        pasta_paginas = os.path.join(os.path.dirname(__file__), "paginas")
        os.makedirs(pasta_paginas, exist_ok=True)

        titulo = entry_titulo.get().strip()
        texto = text_area.get("1.0", tk.END).strip()

        if not titulo:
            titulo = f"pagina_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        else:
            titulo = titulo.replace(" ", "_")
        arquivo_path = os.path.join(pasta_paginas, f"{titulo}.txt")

        with open(arquivo_path, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

        messagebox.showinfo("Salvar Anotação", f"Anotação salva em:\n{arquivo_path}")

    def abrir_paginas():
        pasta_paginas = os.path.join(os.path.dirname(__file__), "paginas")
        if not os.path.exists(pasta_paginas):
            messagebox.showwarning("Abrir Páginas", "Nenhuma página encontrada.")
            return

        arquivos = os.listdir(pasta_paginas)
        if not arquivos:
            messagebox.showwarning("Abrir Páginas", "Nenhuma página encontrada.")
            return

        janela_paginas = tk.Toplevel(janela_anotacoes)
        janela_paginas.title("Páginas Salvas")
        janela_paginas.geometry("600x500")
        janela_paginas.configure(bg="#3E2723")

        tk.Label(
            janela_paginas,
            text="Páginas Salvas:",
            font=("Papyrus", 16, "bold"),
            fg="#FFD700",
            bg="#3E2723"
        ).pack(pady=10)

        listbox_paginas = tk.Listbox(
            janela_paginas,
            font=("Garamond", 12),
            bg="#F5E0C3",
            fg="#000000",
            width=50,
            height=15
        )
        listbox_paginas.pack(pady=10, padx=10)

        for arquivo in arquivos:
            listbox_paginas.insert(tk.END, arquivo)

        def abrir_pagina_selecionada():
            selecionado = listbox_paginas.curselection()
            if not selecionado:
                messagebox.showwarning("Abrir Página", "Nenhuma página selecionada.")
                return

            arquivo_selecionado = listbox_paginas.get(selecionado)
            caminho_arquivo = os.path.join(pasta_paginas, arquivo_selecionado)

            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()

            janela_conteudo = tk.Toplevel(janela_paginas)
            janela_conteudo.title(arquivo_selecionado)
            janela_conteudo.geometry("600x400")
            janela_conteudo.configure(bg="#3E2723")

            text_area_conteudo = tk.Text(
                janela_conteudo,
                font=("Courier", 12),
                bg="#F5E0C3",
                fg="#000000",
                wrap="word",
                insertbackground="#8B0000",
                height=20,
                width=70
            )
            text_area_conteudo.pack(pady=10, padx=10, fill="both", expand=True)
            text_area_conteudo.insert("1.0", conteudo)

        btn_abrir = tk.Button(
            janela_paginas,
            text="Abrir Página",
            command=abrir_pagina_selecionada,
            bg="#228B22",
            fg="white",
            font=("Garamond", 12, "bold"),
            relief="raised",
            activebackground="#32CD32"
        )
        btn_abrir.pack(pady=10)

    # Botões principais
    btn_abrir_paginas = tk.Button(
        janela_anotacoes,
        text="Abrir Páginas",
        command=abrir_paginas,
        bg="#4682B4",
        fg="white",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#5F9EA0"
    )
    btn_abrir_paginas.pack(pady=10)

    btn_salvar = tk.Button(
        janela_anotacoes,
        text="Salvar Anotação",
        command=salvar_anotacao,
        bg="#228B22",
        fg="white",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#32CD32"
    )
    btn_salvar.pack(pady=10)

    btn_fechar = tk.Button(
        janela_anotacoes,
        text="Fechar Grimório",
        command=janela_anotacoes.destroy,
        bg="#8B0000",
        fg="white",
        font=("Garamond", 12, "bold"),
        relief="raised",
        activebackground="#A52A2A"
    )
    btn_fechar.pack(pady=10)
