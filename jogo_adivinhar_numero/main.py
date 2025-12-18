from ferramentas import sortear
import os

def main():
    while True:
        os.system('cls')
        print("--- Jogo da Adivinhação ---")
        try:

            numero_secreto=sortear()

            while True:
                usuario=int(input('Tente adivinhar o número (1-50):'))
                if 1 <= usuario <= 50:
                    break
                print('Digite um número entre 1 e 50.')
                    

            while usuario != numero_secreto:

                if usuario > numero_secreto:
                    print('Número mais alto que o número secreto. Tente um valor MAIS BAIXO!')
                    
                else:
                    print('Número mais baixo que o número secreto. Tente um valor MAIS ALTO!')
                 
                usuario = int(input('Qual seu novo palpite? '))
                    
            
            print(f'Parabéns! Você acertou o número secreto - > {numero_secreto}')

            continuar=input('Deseja continuar? [sim/nao]')
            if continuar.lower() == 'nao':
                print('Programa encerrado!')
                break


        except ValueError:
            input('Entrada inválida: invalid literal for int() with base 10: "abc12"\nDigite qualquer tecla para reiniciar.')



if __name__=='__main__':
    main()
         