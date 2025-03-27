import random

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

    historia = f"{comeco}\n{meio}\n{fim}"
    return historia


print(gerar_historia_npc())