from funcao import identificando
import os 


def main():

    while True:
        os.system('cls')
        print("Identificando palavras > 10 letras.")

        

        entrada=input('Digite uma frase:').strip()

        if not entrada:
            erro=input('Você não digitou nada. Deseja reiniciar o programa? [sim/nao]')
            if erro.lower() =='sim':
                continue
            else:
                print('Programa encerrado. Até breve!')
                break
        if entrada.isdigit():
            print('Digite apenas frases!')
            input('Pressione Enter para reiniciar.')
            continue

        verifica=identificando(entrada)
            
        if verifica:
            print('Palavras longas encontradas:')
            for palavra, qtd in verifica.items():
                print(f'Palavra: {palavra} - Quantidade: {qtd}')
        else:
            print('Não foram encontradas palavras longas.')

        continuar=input('Deseja verificar outra frase? [sim/nao]')
        if continuar.lower() =='nao':
            print('Programa encerrado. Até breve!')
            break

        


if __name__=="__main__":
    main()
