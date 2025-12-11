def identificando(frase):
    palavras_longas={}
    for palavra in frase.split():
        if len(palavra) > 10:
            palavras_longas[palavra]=len(palavra)
    return palavras_longas
