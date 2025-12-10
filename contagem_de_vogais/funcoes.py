
def contando_vogais(frase):
    

    frase_minuscula=frase.lower()

    vogais=["a","e","i","o","u"]
    dicionario_vogais={}
    contador=1
    
    for letra in frase_minuscula:
        if letra in vogais:
            if letra not in dicionario_vogais:
                dicionario_vogais[letra]=contador
            else:
                dicionario_vogais[letra] +=1
    return dicionario_vogais
    
                
                

                    
                    






