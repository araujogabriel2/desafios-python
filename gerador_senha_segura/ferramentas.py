import random

def gerar_senha():
    maiuscula="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula="abcdefghijklmnopqrstuvwxyz"
    numeros="0123456789"
    especiais="!@#$%&*"

    senha=[
        random.choice(maiuscula),
        random.choice(minuscula),
        random.choice(numeros),
        random.choice(especiais)
        ]
    
    todos_caracteres= maiuscula + minuscula + numeros + especiais

    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)










