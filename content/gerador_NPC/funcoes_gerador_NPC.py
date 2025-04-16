import tkinter as tk
from tkinter import ttk, font, messagebox
import random
import customtkinter as ctk

from content.gerador_NPC.content import nomes_masculinos, nomes_femininos, raças, tracos_alinhamento, personalidade, profissoes, defeitos, comecos, meios, fins, organizacoes


def definir_idade(raça):
    if raça == "Elfo":
        idade = random.randint(100, 700)
    elif raça == "Anão":
        idade = random.randint(50, 350)
    elif raça == "Humano":
        idade = random.randint(15, 80)
    elif raça == "Halfling":
        idade = random.randint(20, 150)
    elif raça == "Dragonborn":
        idade = random.randint(15, 80)
    elif raça == "Tiefling":
        idade = random.randint(15, 80)
    elif raça == "Gnomo":
        idade = random.randint(40, 500)
    elif raça == "Orc":
        idade = random.randint(15, 50)
    elif raça == "Aarakocra":
        idade = random.randint(5, 30)
    elif raça == "Aasimar":
        idade = random.randint(15, 100)
    elif raça == "Genasi":
        idade = random.randint(15, 120)
    elif raça == "Goliath":
        idade = random.randint(18, 80)
    elif raça == "Tabaxi":
        idade = random.randint(15, 80)
    elif raça == "Tritão":
        idade = random.randint(20, 200)
    elif raça == "Kenku":
        idade = random.randint(8, 60)
    elif raça == "Firbolg":
        idade = random.randint(30, 500)
    elif raça == "Goblin":
        idade = random.randint(8, 60)
    elif raça == "Hobgoblin":
        idade = random.randint(18, 80)
    elif raça == "Kobold":
        idade = random.randint(10, 120)
    elif raça == "Bugbear":
        idade = random.randint(16, 75)
    elif raça == "Yuan-ti Pureblood":
        idade = random.randint(15, 80)
    elif raça == "Warforged":
        idade = random.randint(15, 1000)  # Valor simbólico
    elif raça == "Shifter":
        idade = random.randint(15, 80)
    elif raça == "Changeling":
        idade = random.randint(5, 80)
    elif raça == "Kalastar":
        idade = random.randint(20, 100)
    elif raça == "Loxodon":
        idade = random.randint(50, 450)
    elif raça == "Simic Hybrid":
        idade = random.randint(15, 80)
    elif raça == "Vedalken":
        idade = random.randint(40, 500)
    elif raça == "Centauro":
        idade = random.randint(20, 100)
    elif raça == "Minotauro":
        idade = random.randint(20, 100)
    elif raça == "Leonin":
        idade = random.randint(20, 100)
    elif raça == "Satyr":
        idade = random.randint(5, 80)
    elif raça == "Harengon":
        idade = random.randint(15, 80)
    elif raça == "Owlin":
        idade = random.randint(15, 100)
    else:
        idade = random.randint(15, 80)

    return idade

def gerar_historia_npc(profissao):


    # Escolha aleatória vinculada à profissão
    comeco = random.choice(comecos.get(profissao, ["Teve uma origem desconhecida."]))
    meio = random.choice(meios.get(profissao, ["Teve uma jornada incomum."]))
    fim = random.choice(fins.get(profissao, ["Teve um destino misterioso."]))
    historia = f"{comeco}. {meio}. {fim}"
    return historia



def gerar_atributos_npc(genero):
    if genero == "Masculino":
        nomeNPC = random.choice(nomes_masculinos)
    else:  # Caso seja "Feminino"
        nomeNPC = random.choice(nomes_femininos)
    
    raça = random.choice(raças)
    alinhamento = random.choice(tracos_alinhamento)
    traço = random.choice(personalidade)
    idade = definir_idade(raça)
    defeito = random.choice(defeitos)

    profissao = random.choice(profissoes)
    organizacao = random.choice(organizacoes)
    
    background = gerar_historia_npc(profissao)


    npc = f"Nome: {nomeNPC}\nRaça: {raça}\nIdade: {idade}\nPersonalidade: {traço}\nDefeitos: {defeito}\nAlinhamento: {alinhamento}\n\nProfissão: {profissao}\nOrganização: {organizacao}\n\nBackground: {background}"
    return npc

# Função para gerar e exibir o NPC
def gerar_npc(root):
    janela_genero = ctk.CTkToplevel(root)
    janela_genero.title("Escolha o Gênero do NPC")
    janela_genero.geometry("350x200")
    janela_genero.configure(fg_color="#D7B377")  
    janela_genero.attributes("-topmost", True)  # Manter a janela no topo
    janela_genero.iconbitmap('icon/shield.ico')  # Definindo o ícone da janela

    def resposta_genero(genero):
        janela_genero.destroy()  # Fecha a janela de seleção
        npc = gerar_atributos_npc(genero)  # Gera os atributos com base no gênero
        exibir_npc(root, npc, genero)  # Exibe o NPC e passa o gênero para regeneração

    label_pergunta = ctk.CTkLabel(
        janela_genero, 
        text="Escolha o gênero do NPC:", 
        font=ctk.CTkFont(family="Garamond", size=20, weight="bold"),
        bg_color="#D7B377",
        text_color="black"


    )
    label_pergunta.pack(pady=15)

    # Botões para seleção de gênero
    btn_masculino = ctk.CTkButton(
        janela_genero, 
        text="Masculino", 
        command=lambda: resposta_genero("Masculino"), 
        width=35,
        fg_color="blue", 
        font=ctk.CTkFont("Garamond", 16, "bold"), 
        hover_color="#00008B",  # Cor ao passar o mouse
        text_color="white"
    )
    btn_masculino.pack(side="left", padx=30, pady=20)

    btn_feminino = ctk.CTkButton(
        janela_genero, 
        text="Feminino", 
        command=lambda: resposta_genero("Feminino"), 
        width=35,
        fg_color="pink", 
        font=ctk.CTkFont("Garamond", 16, "bold"), 
        hover_color="#FF1493",  # Cor ao passar o mouse
        text_color="black"
    )
    btn_feminino.pack(side="right", padx=30, pady=20)

# Função para exibir o NPC gerado
def exibir_npc(root ,npc, genero):
    janela_npc = tk.Toplevel(root)
    janela_npc.title("Ficha do Aventureiro")
    janela_npc.geometry("500x700")
    janela_npc.configure(bg="#D7B377")

    titulo_npc = tk.Label(
        janela_npc, text="-- Ficha do NPC --", font=("Garamond", 18, "bold"),
        bg="#D7B377", fg="#3E2723"
    )
    titulo_npc.pack(pady=10)

    # Moldura para exibir os atributos do NPC
    frame_texto = tk.Frame(janela_npc, bg="#D7B377")
    frame_texto.pack(pady=10, padx=20)

    label_npc = tk.Label(
        frame_texto, text=npc, font=("Garamond", 14), justify="left",
        bg="#FAE5C3", fg="black", relief="groove", padx=10, pady=10, wraplength=400
    )
    label_npc.pack()

    frame_salvar = tk.Frame(janela_npc, bg="#D7B377")
    frame_salvar.pack(pady=10)
    
    

    entrada_arquivo_indicacao = tk.Label(
        janela_npc, text="Digite o nome do arquivo", font=("Garamond", 12, "bold"),
        bg="#D7B377", fg="#3E2723"
    )
    entrada_arquivo_indicacao.pack(pady=10)


    entrada_arquivo = tk.Entry(
        frame_salvar, font=("Garamond", 12), width=20, relief="sunken", 
    )
    entrada_arquivo.pack(side="left", padx=5)


    def salvar_npc():
        nome_arquivo = entrada_arquivo.get().strip()
        if nome_arquivo:
            with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(label_npc.cget("text") + "\n\n" +"Background: ")  # Salva os dados atuais do NPC
            tk.messagebox.showinfo("Salvo", f"NPC salvo em: {nome_arquivo}.txt")
        else:
            tk.messagebox.showwarning("Erro", "Por favor, insira um nome válido para o arquivo.")

    # Função para regenerar os atributos do NPC
    def gerar_novamente():
        novo_npc = gerar_atributos_npc(genero)  # Regenera com base no gênero
        label_npc.config(text=novo_npc)  # Atualiza o texto no Label

    # Botão para gerar o NPC novamente
    btn_gerar_novamente = tk.Button(
        janela_npc, text="Gerar de Novo", command=gerar_novamente,
        bg="#FFA500", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_gerar_novamente.pack(pady=10)

    # Botão para salvar o NPC
    btn_salvar = tk.Button(
        janela_npc, text="Salvar NPC", command=salvar_npc,
        bg="#008CBA", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_salvar.pack(pady=10)

    # Botão para fechar a janela
    btn_fechar = tk.Button(
        janela_npc, text="Fechar", command=janela_npc.destroy,
        bg="#8B0000", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_fechar.pack(pady=10)
