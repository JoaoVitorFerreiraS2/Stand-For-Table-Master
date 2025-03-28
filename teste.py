from tkinter import Tk, Canvas, Button, filedialog
from PIL import Image, ImageDraw

def criar_emblema():
    # Configurações da imagem
    largura, altura = 400, 400
    imagem = Image.new("RGBA", (largura, altura), "white")
    draw = ImageDraw.Draw(imagem)

    # Criar um fundo circular
    draw.ellipse((50, 50, 350, 350), fill="gold", outline="black", width=5)

    # Adicionar ícone central (simulação com um círculo menor)
    draw.ellipse((150, 150, 250, 250), fill="red", outline="black", width=3)

    # Salvar a imagem
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if filepath:
        imagem.save(filepath)

# Configuração da interface
root = Tk()
root.title("Criador de Símbolos")
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

Button(root, text="Criar Emblema", command=criar_emblema).pack(pady=10)
root.mainloop()