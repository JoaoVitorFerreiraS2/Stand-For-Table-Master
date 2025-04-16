from PIL import Image, ImageDraw, ImageOps, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

entry_imagem = None
preview_label = None
imagem_preview = None


def criar_janela_criador_token(root):
    janela_token = tk.Toplevel(root)
    janela_token.title("Criador de Token")
    
    # Configurar o fundo e permitir redimensionamento
    janela_token.configure(bg="#2E2E2E")
    janela_token.resizable(True, True)  # Permite redimensionar

    # Configurar para ocupar a tela inteira (maximizar)
    largura_tela = janela_token.winfo_screenwidth()  # Largura da tela
    altura_tela = janela_token.winfo_screenheight()  # Altura da tela
    janela_token.geometry(f"{largura_tela}x{altura_tela}+0+0")  # Fullscreen ajustável

    criar_interface_token(janela_token)


def criar_token_preview(imagem_path):
    imagem = Image.open(imagem_path).convert("RGBA")
    imagem = ImageOps.fit(imagem, (512, 512))

    # Máscara circular
    mask = Image.new("L", (512, 512), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, 512, 512), fill=255)

    imagem_circular = Image.new("RGBA", (512, 512))
    imagem_circular.paste(imagem, (0, 0), mask=mask)

    # Borda padrão dourada
    borda = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw_borda = ImageDraw.Draw(borda)
    draw_borda.ellipse((5, 5, 507, 507), outline=(255, 215, 0), width=10)

    token_final = Image.alpha_composite(imagem_circular, borda)
    return token_final


def selecionar_imagem():
    global entry_imagem, preview_label, imagem_preview

    imagem_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if imagem_path:
        token_image = criar_token_preview(imagem_path)
        imagem_preview = ImageTk.PhotoImage(token_image)
        preview_label.configure(image=imagem_preview)
        preview_label.image = imagem_preview  # mantém a referência
        entry_imagem.delete(0, tk.END)
        entry_imagem.insert(0, imagem_path)


def salvar_token():
    path = entry_imagem.get()
    if not path:
        messagebox.showerror("Erro", "Selecione uma imagem antes.")
        return

    token = criar_token_preview(path)
    salvar_em = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if salvar_em:
        token.save(salvar_em)
        messagebox.showinfo("Sucesso", "Token salvo com sucesso!")


def criar_interface_token(janela_token):
    global entry_imagem, preview_label

    frame = tk.Frame(janela_token, bg="#2E2E2E")
    frame.pack(pady=20)

    tk.Label(frame, text="Criador de Token", font=("Helvetica", 16, "bold"), bg="#2E2E2E", fg="white").pack(pady=10)

    btn_select = tk.Button(frame, text="Selecionar Imagem", command=selecionar_imagem,
                           bg="#444", fg="white", font=("Arial", 12), width=20)
    btn_select.pack(pady=10)

    entry_imagem = tk.Entry(frame, width=50)
    entry_imagem.pack(pady=5)

    preview_label = tk.Label(janela_token, bg="#2E2E2E")
    preview_label.pack(pady=20)

    btn_save = tk.Button(janela_token, text="Salvar Token", command=salvar_token,
                         bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
    btn_save.pack(pady=10)
