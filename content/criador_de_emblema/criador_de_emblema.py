import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

def criar_emblema():
    """Função para criar e salvar um emblema básico."""
    largura, altura = 400, 400
    imagem = Image.new("RGBA", (largura, altura), "white")
    draw = ImageDraw.Draw(imagem)

    # Criar um fundo circular
    desenhar_fundo(draw, largura, altura)

    # Adicionar um ícone central simulado
    desenhar_icone_central(draw)

    # Salvar o emblema
    salvar_emblema(imagem)

def desenhar_fundo(draw, largura, altura):
    """Desenha o fundo circular do emblema."""
    draw.ellipse((50, 50, largura - 50, altura - 50), fill="gold", outline="black", width=5)

def desenhar_icone_central(draw):
    """Desenha um ícone central (simulado com um círculo menor)."""
    draw.ellipse((150, 150, 250, 250), fill="red", outline="black", width=3)

def salvar_emblema(imagem):
    """Abre a janela para salvar o emblema em um arquivo."""
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if filepath:
        imagem.save(filepath)

def criar_janela_emblema(root):
    """Cria a interface gráfica para interagir com o criador de emblemas."""
    def acao_criar_emblema():
        criar_emblema()

    janela_emblema = tk.Toplevel(root)
    janela_emblema.title("Criador de Símbolos e Emblemas")

    # Configurando a interface gráfica
    tk.Label(janela_emblema, text="Criador de Símbolos e Emblemas", font=("Papyrus", 16, "bold")).pack(pady=10)
    tk.Button(janela_emblema, text="Criar Emblema", font=("Papyrus", 12), command=acao_criar_emblema, bg="#FFD700").pack(pady=20)

    janela_emblema.mainloop()
