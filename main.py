import tkinter as tk
from tkinter import ttk, font, messagebox
import customtkinter as ctk

from content.gerador_NPC.funcoes_gerador_NPC import gerar_npc
from content.balanceamentoCR.balanceamento_CR import balanceamento_CR
from content.economia_contador.economia_contador import criar_janela_moeda
from content.criador_de_emblema.criador_de_emblema import criar_janela_emblema
from content.anotacoes_Mestre.anotacoes_master import criar_janela_anotacoes
from content.criador_token.criador_token import criar_janela_criador_token
from content.icon.ico import ICO_PATH_PRINCIPAL


WIDTH_PRINCIPAL = 850
HEIGHT_PRINCIPAL = 650
WIDTH_BOTAO = 100



# Configuração da janela principal

# root = tk.Tk()
# root.title("Suporte de Mestre - RPG")
# root.configure(bg="#D7B377") 
# root.geometry(f"{WIDTH_PRINCIPAL}x{HEIGHT_PRINCIPAL}")

root = ctk.CTk()
root.iconbitmap(ICO_PATH_PRINCIPAL)  # Definindo o ícone da janela
root.title("Suporte de Mestre - RPG")
root.geometry(f"{WIDTH_PRINCIPAL}x{HEIGHT_PRINCIPAL}")
root.configure(fg_color="#D7B377")  # Cor de fundo
root.resizable(False, False)  # Desabilitando o redimensionamento da janela

font_cabecalho = ctk.CTkFont(family="Garamond", size=30, weight="bold") 
rotulo_cabecalho = ctk.CTkLabel(
    root,    
    text="Suporte de Mestre - RPG",
    font=font_cabecalho,
    bg_color="#D7B377",
    text_color="#3E2723",
    fg_color="#D7B377",
    corner_radius=10,

)
rotulo_cabecalho.pack(pady=20)


# Moldura para separar conteúdo
frame_principal = ctk.CTkFrame(root, bg_color="#D7B377", fg_color="#D7B377")
frame_principal.configure(corner_radius=10)
frame_principal.pack(pady=20)

# Botão estilizado para gerar NPC
btn_gerar_npc = ctk.CTkButton(
    frame_principal,
    text="Gerar NPC",
    width=WIDTH_BOTAO,
    command=lambda: gerar_npc(root),
    bg_color="#8B0000",  # Vermelho escuro para temática RPG
    text_color="white",
    fg_color="#8B0000",
    hover_color="#A52A2A",  # Cor ao passar o mouse
    font=ctk.CTkFont(family="Garamond", size=16, weight="bold"),
    corner_radius=10,

)
btn_gerar_npc.pack(pady=10, padx=10, expand=True)

btn_balanceamento_CR = ctk.CTkButton(
    frame_principal, 
    text="Balanceamento de Combate", 
    width=WIDTH_BOTAO,
    command=lambda: balanceamento_CR(root), 
    bg_color="#8B0000",  # Vermelho escuro para temática RPG
    fg_color="#8B0000",
    hover_color="#A52A2A",  # Cor ao passar o mouse
    text_color="white", 
    font=ctk.CTkFont(family="Garamond", size=16, weight="bold"),    
    corner_radius=10,   
)
btn_balanceamento_CR.pack(pady=10)

conversão_de_moeda = ctk.CTkButton(
    frame_principal, 
    text="Conversão de Moeda", 
    command=lambda: criar_janela_moeda(root), 
    width=WIDTH_BOTAO,
    bg_color="#8B0000",  # Vermelho escuro para temática RPG
    fg_color="#8B0000",
    hover_color="#A52A2A",  # Cor ao passar o mouse
    text_color="white", 
    font=ctk.CTkFont(family="Garamond", size=16, weight="bold"),    
    corner_radius=10,     
)
conversão_de_moeda.pack(pady=10)

criador_de_emblema = ctk.CTkButton(
    frame_principal, 
    text="Criador de Emblema", 
    command=lambda: criar_janela_emblema(root), 
    width=WIDTH_BOTAO,
    bg_color="#8B0000",  # Vermelho escuro para temática RPG
    fg_color="#8B0000",
    hover_color="#A52A2A",  # Cor ao passar o mouse
    text_color="white", 
    font=ctk.CTkFont(family="Garamond", size=16, weight="bold"),    
    corner_radius=10,     
)
criador_de_emblema.pack(pady=10)

# criador_de_token = ctk.CTkButton(
#     frame_principal, 
#     text="Criador de Token", 
#     command=lambda: criar_janela_criador_token(root),
#     width=WIDTH_BOTAO, 
#     bg_color="#8B0000",  # Vermelho escuro para temática RPG
#     fg_color="#8B0000",
#     hover_color="#A52A2A",  # Cor ao passar o mouse
#     text_color="white", 
#     font=ctk.CTkFont(family="Garamond", size=16, weight="bold"),    
#     corner_radius=10,     
# )
# criador_de_token.pack(pady=10)

# anotacoes_mestre = tk.Button(
#     frame_principal, 
#     text="Anotações do Mestre", 
#     command=lambda: criar_janela_anotacoes(root), 
#     bg="#8B0000",  # Vermelho escuro para temática RPG
#     fg="white", 
#     font=("Garamond", 14, "bold"),
#     relief="raised"   
# )
# anotacoes_mestre.pack(pady=10)

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
    font=("Garamond", 16, "italic"), 
    bg="#D7B377", 
    fg="#3E2723"
)
rodape.pack(side="bottom", pady=10)

rodape = tk.Label(
    root, 
    text="""
        Criado por João Vitor""", 
    font=("Garamond", 12, "italic"), 
    bg="#D7B377", 
    fg="#3E2723"
)
rodape.pack(side="left", pady=10)

root.mainloop()