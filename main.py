import tkinter as tk
from tkinter import ttk, font, messagebox
import random


WIDTH_PRINCIPAL = 850
HEIGHT_PRINCIPAL = 650

# Listas para os atributos do NPC
nomes_masculinos = [
    "Alfarr", "Martius", "Boris", "Karl", "Gerwald", "Rodger", "Herbet", "Ravi", "Arnoald", "Magno",
    "Héktor", "Yngvarr", "Darlan", "Vicenzo", "Liam", "Hloddoviko", "Damian", "Elmo", "Níke",
    "Mackeswell", "Absalom", "Rayyan", "Yudi", "Armstrong", "Friedrich", "Apólo", "Zeus",
    "Maximilian", "Renatus", "Argos", "Hélio", "Benedictus", "Adônis", "Orion", "Atlas",
    "Ícarus", "Herácles", "Théos", "Andreas", "Ambrose", "Harry", "Lazar", "Relic", "Balthazar",
    "Wilfred", "Kuron", "Menw", "Severus", "Linus", "Barron", "Garon", "Alister", "Kiano",
    "Pierce", "Rune", "Percival", "Merlin", "Potter", "Lux", "Zadock", "Wolcott", "Dune", "Eris",
    "Gandalf", "Nimbus", "Elric", "Puck", "Phinneas", "Remus", "Rubeus", "Circle", "Paulinus",
    "Lucius", "Saruman", "Mix", "Alatar", "Jafar", "Seamus", "Atlantes", "Prospero", "Ganondorf",
    "Radagast", "Hendrick", "Pallando", "Robaldo", "Roland", "Hunter", "Venâncio", "Monteiro",
    "Kurama", "Kaled", "Aprígio", "Chase", "Orion", "Garrido", "Ninrode", "Stephanus", "Hunt",
    "Logon", "Garret", "Elladan", "Iston", "Earendil", "Haldir", "Nessa", "Idril", "Legolas",
    "Callon", "Estel", "Poldon", "Amis", "Bentley", "Dalibor", "Arthurus", "Bjørn", "Håkon",
    "Richard", "Dragomir", "Frederick", "Hawise", "Arvydas", "Edward", "Enguerrand", "Domenico",
    "Archer", "Apollo", "Hanzo", "Flecheiro", "Hankyu", "Mirador", "Arash", "Houyi", "Certeiro",
    "Robin Hood", "Eros", "Radagásio", "Golyla", "Oskar", "Draco", "Leviatan", "Smaug", "Ghidorah",
    "Ryoko", "Safira", "Drakon", "Shin", "Fuyuki", "Lázarus", "Krueger", "Thanos", "Joker"
]

nomes_femininos = [
    "Marcella", "Celina", "Ailène", "Pilar", "Chlodovech", "Luana", "Níkaia", "Hilda", "Dandara",
    "Mahthildis", "Alma", "Ioná", "Héloïse", "Itília", "Zoé", "Lot-regne", "Cibele", "Saori",
    "Maia", "Carolaine", "Sakura", "Natalis", "Asha", "Valentina", "Aurora", "Aruna", "Gaia",
    "Gertrudes", "Nadine", "Imani", "Íres", "Philoméne", "Dione", "Phoebe", "Têmis", "Salomé",
    "Afrodite", "Pandora", "Alaska", "Pérola", "Jacinta", "Ariadne", "Erhais", "Anastásia",
    "Jocasta", "Dafne", "Barbar", "Esperanza", "Athena", "Ártemis", "Pan", "Cassandra", "Agnes",
    "Gwydion", "Gwen", "Joane", "Laurie", "Leanne", "Raven", "Margaret", "Medea", "Morgana",
    "Ursula", "Narcisa", "Calypso", "Euterpe", "Bathilda", "Andromeda", "Polímnia", "Margery",
    "Clio", "Asterope", "Ravenna", "Elphaba", "Glenda", "Melpômene", "Calíope", "Malévola",
    "Blanche", "Terpsícore", "Ginevra", "Minerva", "Elladora", "Winifred", "Endora", "Meliflua",
    "Apolline", "Bellatrix", "Elfrinda", "Dilys", "Artemis", "Gisely", "Amazonas", "Gisa",
    "Lightwood", "Elvira", "Katniss", "Skaði", "Zoé", "Afrodite"
]

raças = [
    "Humano",
    "Elfo",
    "Anão",
    "Halfling",
    "Dragonborn",
    "Tiefling",
    "Gnomo",
    "Orc",
    "Aarakocra",
    "Aasimar",
    "Genasi (Ar, Água, Fogo, Terra)",
    "Goliath",
    "Tabaxi",
    "Tritão",
    "Kenku",
    "Firbolg",
    "Goblin",
    "Hobgoblin",
    "Kobold",
    "Bugbear",
    "Yuan-ti Pureblood",
    "Warforged",
    "Shifter",
    "Changeling",
    "Kalastar",
    "Loxodon",
    "Simic Hybrid",
    "Vedalken",
    "Centauro",
    "Minotauro",
    "Leonin",
    "Satyr",
    "Harengon",
    "Owlin"
]
personalidade = [
    "Valente", "Astuto", "Impulsivo", "Reservado", "Carismático", "Curioso", "Determinado",
    "Egoísta", "Generoso", "Imprevisível", "Metódico", "Pessimista", "Realista", "Sonhador",
    "Teimoso", "Tranquilo", "Sarcástico", "Prudente", "Extrovertido", "Introvertido",
    "Amigável", "Desconfiado", "Ambicioso", "Altruísta", "Obstinado", "Indeciso", "Inquieto",
    "Focado", "Calculista", "Excêntrico", "Justo", "Manipulador", "Pacífico", "Optimista",
    "Rabugento", "Espontâneo", "Assertivo", "Compreensivo", "Ingênuo", "Cauteloso", "Empático"
]

profissoes = [
    "Ferreiro", "Alquimista", "Mercador", "Camponês", "Taberneiro", "Sacerdote",
    "Guarda", "Caçador", "Carpinteiro", "Arqueólogo", "Escrivão", "Minerador",
    "Costureiro", "Cavaleiro", "Curandeiro", "Músico", "Herborista", "Navegador",
    "Bardo", "Cartógrafo", "Taverneiro", "Ladrão", "Espião", "Artista",
    "Soldado", "Construtor", "Explorador", "Bibliotecário", "Professor",
    "Engenheiro", "Diplomata", "Chapeleiro", "Ourives", "Boticário", "Agricultor",
    "Cientista", "Marinheiro", "Coveiro", "Advogado", "Estalajadeiro",
    "Estudioso", "Inventor", "Mago", "Pescador", "Caixeiro Viajante", "Joalheiro",
    "Apicultor", "Domador de Animais", "Caçador de Recompensas", "Cartomante",
    "Escultor", "Padeiro", "Cervejeiro", "Lavrador", "Lenhador", "Açougueiro"
]

tracos_alinhamento = [
    # Alinhamentos bons
    "Leal e Bom",   # Segue regras e leis, agindo de maneira altruísta.
    "Neutro e Bom", # Faz o bem, independente de regras ou leis.
    "Caótico e Bom", # Faz o bem de forma espontânea, sem seguir normas ou tradições.

    # Alinhamentos neutros
    "Leal e Neutro", # Segue as leis, regras ou tradições, mas sem uma inclinação clara para o bem ou o mal.
    "Neutro",        # Mantém equilíbrio, não se inclina para o bem ou o mal.
    "Caótico e Neutro", # Prioriza liberdade e imprevisibilidade acima de tudo, sem alinhar-se ao bem ou ao mal.

    # Alinhamentos maus
    "Leal e Mau",    # Segue um código ou ordem, mas com intenções maléficas.
    "Neutro e Mau",  # Faz o mal de forma pragmática, sem apegos a regras ou caos.
    "Caótico e Mau"  # Faz o mal de forma desorganizada e imprevisível.
]

defeitos = [
    "Sem braço", "Cicatriz no rosto", "Gago", "Cego de um olho", "Manqueira",
    "Surdo", "Sem dedos em uma mão", "Pele queimada", "Nariz quebrado",
    "Dentes faltando", "Cabelo ralo", "Respiração ofegante", "Mãos trêmulas",
    "Postura encurvada", "Rosto deformado", "Voz rouca", "Cicatriz no pescoço",
    "Pé torto", "Caminha com bengala", "Falta de equilíbrio", "Fala arrastada",
    "Tosse crônica", "Mãos calejadas", "Rosto sem expressão", "Cicatriz na testa",
    "Cicatriz na perna", "Caminha com dificuldade", "Pele manchada", "Queimadura na mão",
    "Rosto com marcas de batalha", "Dedos amputados", "Olhos fundos", "Mãos ásperas",
    "Caminhar arrastado", "Cicatriz profunda no braço", "Pele com marcas de queimadura",
    "Braço enfaixado", "Cicatriz que atravessa o olho", "Rosto franzido permanentemente", "Super Espinhas"
]

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

def gerar_historia_npc():
    # Opções para cada parte da história
    comecos = [
        "Nasceu em uma aldeia remota cercada por florestas densas.",
        "Foi criado por uma guilda de ladrões após ser abandonado.",
        "Era um ferreiro talentoso conhecido por suas obras excepcionais.",
        "Cresceu em uma corte real como servo de nobres.",
        "Descobriu poderes mágicos ainda na juventude."
    ]

    meios = [
        "Decidiu se aventurar em busca de respostas sobre seu passado.",
        "Foi traído por um amigo e agora busca vingança.",
        "Envolveu-se em um conflito entre duas facções poderosas.",
        "Encontrou um artefato mágico que mudou sua vida para sempre.",
        "Unificou um grupo de aventureiros para enfrentar uma ameaça comum."
    ]

    fins = [
        "Sacrificou-se para proteger sua vila de uma invasão.",
        "Ascendeu ao status de herói após salvar o reino.",
        "Tornou-se um líder respeitado de sua guilda.",
        "Desapareceu misteriosamente enquanto explorava uma ruína antiga.",
        "Viveu seus dias em paz, compartilhando suas histórias com os mais jovens."
    ]

    # Escolha aleatória de cada parte
    comeco = random.choice(comecos)
    meio = random.choice(meios)
    fim = random.choice(fins)

    historia = f"{comeco}. {meio}.{fim}"
    return historia



def gerar_atributos_npc(genero):
    if genero == "Masculino":
        nomeNPC = random.choice(nomes_masculinos)
    else:  # Caso seja "Feminino"
        nomeNPC = random.choice(nomes_femininos)
    
    raça = random.choice(raças)
    alinhamento = random.choice(tracos_alinhamento)
    traço = random.choice(personalidade)
    profissao = random.choice(profissoes)
    idade = definir_idade(raça)
    defeito = random.choice(defeitos)
    #background = gerar_historia_npc()


    npc = f"Nome: {nomeNPC}\nRaça: {raça}\nIdade: {idade}\nPersonalidade: {traço}\nDefeitos: {defeito}\nAlinhamento: {alinhamento}\n\nProfissão: {profissao}"
    return npc

# Função para gerar e exibir o NPC
def gerar_npc():
    janela_genero = tk.Toplevel(root)
    janela_genero.title("Escolha o Gênero do NPC")
    janela_genero.geometry("350x200")
    janela_genero.configure(bg="#D7B377")  

    def resposta_genero(genero):
        janela_genero.destroy()  # Fecha a janela de seleção
        npc = gerar_atributos_npc(genero)  # Gera os atributos com base no gênero
        exibir_npc(npc, genero)  # Exibe o NPC e passa o gênero para regeneração

    label_pergunta = tk.Label(
        janela_genero, 
        text="Escolha o gênero do NPC:", 
        font=("Garamond", 16, "bold"), 
        bg="#D7B377", 
        fg="#3E2723"
    )
    label_pergunta.pack(pady=15)

    # Botões para seleção de gênero
    btn_masculino = tk.Button(
        janela_genero, 
        text="Masculino", 
        command=lambda: resposta_genero("Masculino"), 
        bg="#4CAF50", fg="white", font=("Garamond", 14, "bold"), relief="raised"
    )
    btn_masculino.pack(side="left", padx=30, pady=20)

    btn_feminino = tk.Button(
        janela_genero, 
        text="Feminino", 
        command=lambda: resposta_genero("Feminino"), 
        bg="#FF6347", fg="white", font=("Garamond", 14, "bold"), relief="raised"
    )
    btn_feminino.pack(side="right", padx=30, pady=20)

# Função para exibir o NPC gerado
def exibir_npc(npc, genero):
    janela_npc = tk.Toplevel(root)
    janela_npc.title("Ficha do Aventureiro")
    janela_npc.geometry("450x500")
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



def balanceamento_CR():
    janela_CR = tk.Toplevel(root)
    janela_CR.title("Balanceamento de Encontros")
    janela_CR.geometry("400x350")
    janela_CR.configure(bg="#D7B377")

    # Título estilizado
    label_pergunta = tk.Label(
        janela_CR, 
        text="Informe os dados do grupo:", 
        font=("Garamond", 16, "bold"), 
        bg="#D7B377", 
        fg="#3E2723"
    )
    label_pergunta.pack(pady=15)

    # Frame para entradas
    frame_sobre_equipe = tk.Frame(janela_CR, bg="#D7B377")
    frame_sobre_equipe.pack(pady=10)

    # Entrada: Quantidade de jogadores
    qtd_equipe_indicacao = tk.Label(
        frame_sobre_equipe, 
        text="Quantidade de jogadores:", 
        font=("Garamond", 12, "bold"), 
        bg="#D7B377", 
        fg="#3E2723"
    )
    qtd_equipe_indicacao.pack(pady=5)
    qtd_equipe = tk.Entry(
        frame_sobre_equipe, font=("Garamond", 12), width=5, relief="sunken"
    )
    qtd_equipe.pack(pady=5)

    # Entrada: Nível médio dos jogadores
    nvl_equipe_indicacao = tk.Label(
        frame_sobre_equipe, 
        text="Nível médio dos jogadores:", 
        font=("Garamond", 12, "bold"), 
        bg="#D7B377", 
        fg="#3E2723"
    )
    nvl_equipe_indicacao.pack(pady=5)
    nvl_equipe = tk.Entry(
        frame_sobre_equipe, font=("Garamond", 12), width=5, relief="sunken"
    )
    nvl_equipe.pack(pady=5)

    # Função para calcular os desafios
    def calcular_balanceamento():
        try:
            # Coletar os dados inseridos pelo usuário
            num_jogadores = int(qtd_equipe.get())
            nivel_grupo = int(nvl_equipe.get())

            # Validar entradas
            if num_jogadores <= 0 or nivel_grupo <= 0:
                tk.messagebox.showwarning("Erro", "Os valores devem ser maiores que zero!")
                return

            # Cálculo de inimigos por dificuldade
            dificuldades = {
                "Luta Fácil": 0.5,
                "Luta Balanceada": 1,
                "Luta Difícil": 1.5,
                "Luta Mortal": 2
            }

            resultados = []
            for dificuldade, modificador in dificuldades.items():
                cr_recomendado = nivel_grupo * modificador
                quantidade_inimigos = max(1, num_jogadores // modificador)
                resultados.append(f"{dificuldade}: Utilize {int(quantidade_inimigos)} monstros de CR {int(cr_recomendado)}")

            # Nova janela para exibir os resultados
            janela_resultado = tk.Toplevel(root)
            janela_resultado.title("Sugestões de Encontro")
            janela_resultado.geometry("400x300")
            janela_resultado.configure(bg="#D7B377")

            # Título da janela de resultados
            label_resultado = tk.Label(
                janela_resultado, 
                text="Sugestões de Encontro", 
                font=("Garamond", 16, "bold"), 
                bg="#D7B377", 
                fg="#3E2723"
            )
            label_resultado.pack(pady=10)

            # Exibição das sugestões
            for resultado in resultados:
                resultado_label = tk.Label(
                    janela_resultado, 
                    text=resultado, 
                    font=("Garamond", 12), 
                    bg="#FAE5C3", 
                    fg="black", 
                    relief="groove", 
                    padx=10, 
                    pady=5
                )
                resultado_label.pack(pady=5)

            # Botão para fechar a janela
            btn_fechar_resultado = tk.Button(
                janela_resultado, text="Fechar", command=janela_resultado.destroy,
                bg="#8B0000", fg="white", font=("Garamond", 12, "bold"), relief="raised"
            )
            btn_fechar_resultado.pack(pady=10)

        except ValueError:
            tk.messagebox.showerror("Erro", "Por favor, insira números válidos!")

    # Botão para calcular
    btn_calcular = tk.Button(
        janela_CR, text="Calcular", command=calcular_balanceamento,
        bg="#008CBA", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_calcular.pack(pady=10)

    # Botão para fechar
    btn_fechar = tk.Button(
        janela_CR, text="Fechar", command=janela_CR.destroy,
        bg="#8B0000", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_fechar.pack(pady=10)


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
    command=gerar_npc, 
    bg="#8B0000",  # Vermelho escuro para temática RPG
    fg="white", 
    font=("Garamond", 14, "bold"),
    relief="raised"  # Toque medieval 
)
btn_gerar_npc.pack(pady=10)

btn_balanceamento_CR = tk.Button(
    frame_principal, 
    text="Balanceamento de Combate", 
    command=balanceamento_CR, 
    bg="#8B0000",  # Vermelho escuro para temática RPG
    fg="white", 
    font=("Garamond", 14, "bold"),
    relief="raised"   
)
btn_balanceamento_CR.pack(pady=10)

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

root.mainloop()