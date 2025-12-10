from funcoes import contando_vogais
import os 

def main():

    print("Contando vogais")
    while True:
        os.system('cls')
        entrada_frase=input('Digite uma frase:')

        if not entrada_frase:
            print('Você não digitou nada.')
            input('Aperte Enter para tentar novamente..')
            continue

        saida=contando_vogais(entrada_frase)

        if saida:
            for vogal, qtd in saida.items():
                print(f'Vogal: {vogal} - Quantidade: {qtd}x')
        
        
        opcao=input('Deseja contar mais vogais em outras frases? [sim/nao]\nObs: Aperte qualquer tecla para reiniciar:')
        
        if opcao.lower() =='nao':
            print('Programa encerrado.')
            break





if __name__=='__main__':
    main()

