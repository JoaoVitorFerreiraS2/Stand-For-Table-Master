import tkinter as tk
from tkinter import ttk, font, messagebox

from content.gerador_NPC.funcoes_gerador_NPC import gerar_npc


WIDTH_PRINCIPAL = 850
HEIGHT_PRINCIPAL = 650


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