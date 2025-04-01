import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import random

def criar_emblema():
    """Cria um emblema estilizado com formatos e cores aleatórios."""
    largura, altura = 400, 400
    imagem = Image.new("RGBA", (largura, altura), "white")
    draw = ImageDraw.Draw(imagem)

    # Criar fundo degradê com cores aleatórias
    desenhar_fundo_gradiente(imagem, draw, largura, altura)

    # Criar escudo com formato aleatório
    desenhar_escudo(draw, largura, altura)

    # Adicionar padrões simétricos com cores aleatórias
    desenhar_padroes(draw, largura, altura)

    return imagem

def desenhar_fundo_gradiente(imagem, draw, largura, altura):
    """Desenha um fundo degradê com cores aleatórias."""
    cor1 = random.choice([(255, 140, 0), (255, 0, 0), (0, 255, 127), (75, 0, 130),
 (0, 191, 255), (123, 104, 238), (255, 20, 147), (34, 139, 34),
 (240, 230, 140), (72, 61, 139), (47, 79, 79), (210, 105, 30),
 (173, 216, 230), (244, 164, 96), (199, 21, 133), (154, 205, 50),
 (0, 128, 128), (255, 165, 0), (128, 0, 128), (0, 100, 0),
 (70, 130, 180), (205, 92, 92), (255, 215, 0), (139, 69, 19),
 (218, 112, 214), (0, 0, 255), (138, 43, 226), (152, 251, 152),
 (128, 128, 0), (250, 128, 114), (0, 255, 255), (105, 105, 105),
 (186, 85, 211), (240, 128, 128), (50, 205, 50), (220, 20, 60)]
)
    cor2 = random.choice([(255, 140, 0), (255, 0, 0), (0, 255, 127), (75, 0, 130),
 (0, 191, 255), (123, 104, 238), (255, 20, 147), (34, 139, 34),
 (240, 230, 140), (72, 61, 139), (47, 79, 79), (210, 105, 30),
 (173, 216, 230), (244, 164, 96), (199, 21, 133), (154, 205, 50),
 (0, 128, 128), (255, 165, 0), (128, 0, 128), (0, 100, 0),
 (70, 130, 180), (205, 92, 92), (255, 215, 0), (139, 69, 19),
 (218, 112, 214), (0, 0, 255), (138, 43, 226), (152, 251, 152),
 (128, 128, 0), (250, 128, 114), (0, 255, 255), (105, 105, 105),
 (186, 85, 211), (240, 128, 128), (50, 205, 50), (220, 20, 60)])
    
    
    for i in range(altura):
        cor = (
            int(cor1[0] + (cor2[0] - cor1[0]) * (i / altura)),
            int(cor1[1] + (cor2[1] - cor1[1]) * (i / altura)),
            int(cor1[2] + (cor2[2] - cor1[2]) * (i / altura)),
        )
        draw.line([(0, i), (largura, i)], fill=cor)

def desenhar_escudo(draw, largura, altura):
    """Desenha um escudo com formato e cor aleatórios."""
    cor_escudo = random.choice(["red", "blue", "green", "purple", "black", "gold", "silver",
    "orange", "yellow", "cyan", "pink", "white", "gray", "teal",
    "magenta", "lime", "brown", "navy", "indigo", "violet", "beige",
    "coral", "turquoise", "ivory", "khaki", "salmon", "maroon", "lavender",
    "plum"]
)
    formato = random.choice(["triangular", "oval", "hexagonal", "retangular", "diamante", "estrela"])
    tamanho = random.randint(0, 5)

    if formato == "triangular":
        pontos = [(largura // 2, altura // 4), (largura // 4, altura - 100), (3 * largura // 4, altura - 100)]
        draw.polygon(pontos, fill=cor_escudo, outline="black", width=tamanho)

    elif formato == "oval":
        draw.ellipse([(largura // 4, altura // 4), (3 * largura // 4, 3 * altura // 4)], fill=cor_escudo, outline="black", width=5)

    elif formato == "hexagonal":
        pontos = [(largura // 2 - 80, altura // 4), (largura // 2 + 80, altura // 4),
                  (largura // 2 + 100, altura // 2), (largura // 2 + 80, altura - 100),
                  (largura // 2 - 80, altura - 100), (largura // 2 - 100, altura // 2)]
        draw.polygon(pontos, fill=cor_escudo, outline="black", width=tamanho)

    elif formato == "retangular":
        draw.rectangle([(largura // 4, altura // 4), (3 * largura // 4, 3 * altura // 4)], fill=cor_escudo, outline="black", width=5)

    elif formato == "diamante":
        pontos = [(largura // 2, altura // 4), (3 * largura // 4, altura // 2),
                  (largura // 2, 3 * altura // 4), (largura // 4, altura // 2)]
        draw.polygon(pontos, fill=cor_escudo, outline="black", width=tamanho)

    elif formato == "estrela":
        pontos = [(largura // 2, altura // 4), (largura // 2 + 30, altura // 2 - 20),
                  (largura // 2 + 80, altura // 2), (largura // 2 + 30, altura // 2 + 20),
                  (largura // 2, 3 * altura // 4), (largura // 2 - 30, altura // 2 + 20),
                  (largura // 2 - 80, altura // 2), (largura // 2 - 30, altura // 2 - 20)]
        draw.polygon(pontos, fill=cor_escudo, outline="black", width=tamanho)
    
    elif formato == "dupla_ponta":
        pontos = [(largura // 2, altura // 4), (3 * largura // 4, altura // 2 - 20),
                  (largura // 2 + 80, altura - 100), (largura // 2, altura - 60),
                  (largura // 2 - 80, altura - 100), (largura // 4, altura // 2 - 20)]
        draw.polygon(pontos, fill=cor_escudo, outline="black", width=tamanho)

def desenhar_padroes(draw, largura, altura):
    """Adiciona padrões simétricos ao emblema com cores aleatórias."""
    cores = ["white", "gold", "silver", "cyan", "pink"]
    for i in range(random.randint(2, 4)):
        x = largura // 2
        y = altura // 3 + i * 50
        tamanho = random.randint(20, 50)
        draw.ellipse(
            (x - tamanho, y - tamanho, x + tamanho, y + tamanho),
            fill=random.choice(cores), outline="black", width=3
        )

def exibir_emblema(root, label_imagem):
    """Exibe o emblema na interface gráfica, substituindo o anterior."""
    imagem = criar_emblema()
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem.config(image=imagem_tk)
    label_imagem.imagem_tk = imagem_tk  

def criar_janela_emblema(root):
    """Cria a interface gráfica para interagir com o criador de emblemas."""
    janela_emblema = tk.Toplevel(root)
    janela_emblema.title("Criador de Emblemas")
    janela_emblema.geometry("700x600")

    tk.Label(janela_emblema, text="Criador de Emblemas", font=("Arial", 16, "bold")).pack(pady=10)
    
    label_imagem = tk.Label(janela_emblema)
    label_imagem.pack(pady=20)
    
    tk.Button(janela_emblema, text="Gerar Emblema", font=("Arial", 12), 
              command=lambda: exibir_emblema(janela_emblema, label_imagem), bg="#FFD700").pack(pady=20)

#Está faltando a droga do botão salvar, esqueci :(