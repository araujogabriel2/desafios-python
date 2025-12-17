import random 

def escolha_computador():
    opcoes=['pedra', 'papel', 'tesoura']
    sortir=random.choice(opcoes)
    return sortir 

def verificar_vencedor(jogador, computador):
    # ganha : perde
    regras = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra"
    }

    if jogador == computador:
        return "Empate!"
    elif regras[jogador] == computador:
        return 'Você venceu!'
    else:
        return 'Você perdeu!'






