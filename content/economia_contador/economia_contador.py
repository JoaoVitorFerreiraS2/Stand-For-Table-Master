import tkinter as tk

def criar_janela_moeda(root):
    def calcular_valor():
        try:
            # Recuperando os valores da entrada
            valor_unitario = float(entry_valor_unitario.get())
            quantidade = int(entry_quantidade.get())
            total = valor_unitario * quantidade

            if total < 0:
                resultado_label.config(text="Engraçadinho você em")
            
            else:
                # Definindo o tipo de moeda selecionada
                if moeda_selecionada.get() == "cobre":
                    # Conversão de cobre para moedas maiores
                    prata = int(total // 10)
                    cobre = total % 10
                    ouro = prata // 10
                    prata = prata % 10
                    resultado_label.config(text=f"Total: {ouro} ouro(s), {prata} prata(s), {cobre:.0f} cobre(s)")
                elif moeda_selecionada.get() == "prata":
                    ouro = int(total // 10)
                    prata = total % 10
                    resultado_label.config(text=f"Total: {ouro} ouro(s), {prata:.0f} prata(s)")
                elif moeda_selecionada.get() == "ouro":
                    platina = int(total // 10)
                    ouro = total % 10
                    resultado_label.config(text=f"Total: {platina} platina(s), {ouro:.0f} ouro(s)")
                elif moeda_selecionada.get() == "platina":
                    resultado_label.config(text=f"Total: {total:.0f} platina(s)")
                else:
                    resultado_label.config(text="Selecione uma moeda válida!")
        except ValueError:
            resultado_label.config(text="Está zombando da minha cara?")

    # Criando a janela principal
    janela_economia = tk.Toplevel(root)
    janela_economia.title("Contador de Moedas D&D")
    janela_economia.configure(bg="#8B4513") 
    janela_economia.geometry("600x600")

    # Variável vinculada aos Radiobuttons
    moeda_selecionada = tk.StringVar(value="cobre") 

    # Campo para selecionar a moeda
    tk.Label(janela_economia, text="Selecione a moeda base:", font=("Papyrus", 12), bg="#8B4513", fg="white").pack(pady=5)
    tk.Radiobutton(janela_economia, text="Cobre", variable=moeda_selecionada, value="cobre", font=("Papyrus", 10), bg="brown", fg="black", width=10, indicatoron=0).pack(pady=2)
    tk.Radiobutton(janela_economia, text="Prata", variable=moeda_selecionada, value="prata", font=("Papyrus", 10), bg="silver", fg="black", width=10, indicatoron=0).pack(pady=2)
    tk.Radiobutton(janela_economia, text="Ouro", variable=moeda_selecionada, value="ouro", font=("Papyrus", 10), bg="gold", fg="black", width=10, indicatoron=0).pack(pady=2)
    tk.Radiobutton(janela_economia, text="Platina", variable=moeda_selecionada, value="platina", font=("Papyrus", 10), bg="purple", fg="black", width=10, indicatoron=0).pack(pady=2)

    # Criando os campos de entrada
    tk.Label(janela_economia, text="Valor Unitário:", font=("Papyrus", 12), bg="#8B4513", fg="white").pack(pady=5)
    entry_valor_unitario = tk.Entry(janela_economia, font=("Papyrus", 12), justify="center")
    entry_valor_unitario.pack(pady=5)

    tk.Label(janela_economia, text="Quantidade:", font=("Papyrus", 12), bg="#8B4513", fg="white").pack(pady=5)
    entry_quantidade = tk.Entry(janela_economia, font=("Papyrus", 12), justify="center")
    entry_quantidade.pack(pady=5)

    # Botão para calcular
    btn_calcular = tk.Button(janela_economia, text="Calcular", font=("Papyrus", 12), bg="#FFD700", fg="black", command=calcular_valor)
    btn_calcular.pack(pady=10)

    btn_fechar = tk.Button(
        janela_economia, text="Fechar", command=janela_economia.destroy,
        bg="#8B0000", fg="white", font=("Garamond", 12, "bold"), relief="raised"
    )
    btn_fechar.pack(pady=10)

    # Label para exibir o resultado
    resultado_label = tk.Label(janela_economia, text="", font=("Papyrus", 14, "bold"), bg="#8B4513", fg="#FFD700")
    resultado_label.pack(pady=20)

    

    
    # Adicionando uma borda decorativa
    tk.Label(janela_economia, text="Banco Real das Moedas", font=("Papyrus", 18, "bold"), bg="#8B4513", fg="gold").pack(pady=10)

    # Iniciando o loop da interface
    janela_economia.mainloop()