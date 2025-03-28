import tkinter as tk
from tkinter import ttk, font, messagebox

from content.gerador_NPC.funcoes_gerador_NPC import gerar_npc
from content.balanceamentoCR.balanceamento_CR import balanceamento_CR
from content.economia_contador.economia_contador import criar_janela

WIDTH_PRINCIPAL = 850
HEIGHT_PRINCIPAL = 650



# Configuração da janela principal

root = tk.Tk()
root.title("Suporte de Mestre - RPG")
root.configure(bg="#D7B377") 
root.geometry(f"{WIDTH_PRINCIPAL}x{HEIGHT_PRINCIPAL}")

font_cabecalho = font.Font(family="Garamond", size=30, weight="bold")
rotulo_cabecalho = tk.Label(
    root, 
    text="Suporte de Mestre - RPG", 
    font=font_cabecalho, 
    bg="#D7B377", 
    fg="#3E2723" 
)
rotulo_cabecalho.pack(pady=20)

# Moldura para separar conteúdo
frame_principal = tk.Frame(root, bg="#D7B377")
frame_principal.pack(pady=20)

# Botão estilizado para gerar NPC
btn_gerar_npc = tk.Button(
    frame_principal, 
    text="Gerar NPC", 
    command=lambda: gerar_npc(root), 
    bg="#8B0000",  # Vermelho escuro para temática RPG
    fg="white", 
    font=("Garamond", 14, "bold"),
    relief="raised"  # Toque medieval 
)
btn_gerar_npc.pack(pady=10)

btn_balanceamento_CR = tk.Button(
    frame_principal, 
    text="Balanceamento de Combate", 
    command=lambda: balanceamento_CR(root), 
    bg="#8B0000",  # Vermelho escuro para temática RPG
    fg="white", 
    font=("Garamond", 14, "bold"),
    relief="raised"   
)
btn_balanceamento_CR.pack(pady=10)

conversão_de_moeda = tk.Button(
    frame_principal, 
    text="Conversão de Moeda", 
    command=lambda: criar_janela(root), 
    bg="#8B0000",  # Vermelho escuro para temática RPG
    fg="white", 
    font=("Garamond", 14, "bold"),
    relief="raised"   
)
conversão_de_moeda.pack(pady=10)

# Oração SAGRADA, NUNCA APAGUE OU SUA MESA SERÁ AZARADA PARA SEMPRE
rodape = tk.Label(
    root, 
    text="""
        Que os dados rolem sem hesitar,
        Que nenhum mestre seja desafiado por regras que não viu;
        Que nossas mesas sejam sagradas como altares de imaginação.
        Que os jogadores tragam histórias, não apenas disputas.
        Que a regra da casa seja respeitada,
        E que a criatividade nunca seja subjugada pelo manual.
        Que cada NPC tenha seu momento,
        E cada vilão receba um final digno.
        Que o improviso nos salve do imprevisível,
        E que nossas campanhas sejam épicas, não esquecidas.
        Que o escudo do mestre proteja seu reino de energia desnecessária!""", 
    font=("Garamond", 10, "italic"), 
    bg="#D7B377", 
    fg="#3E2723"
)
rodape.pack(side="bottom", pady=10)

rodape = tk.Label(
    root, 
    text="""
        Criado por João Vitor""", 
    font=("Garamond", 10, "italic"), 
    bg="#D7B377", 
    fg="#3E2723"
)
rodape.pack(side="left", pady=10)

root.mainloop()