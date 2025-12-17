from ferramentas import escolha_computador, verificar_vencedor
import os
import time 

def main():
    
    while True:
        os.system('cls')
        print("🅹🅾🅶🅾: 🅿🅴🅳🆁🅰, 🅿🅰🅿🅴🅻 🅴 🆃🅴🆂🅾🆄🆁🅰")

        permitidos=['pedra', 'papel', 'tesoura']

        entrada=input('Escolha um ataque -> [pedra/papel/tesoura] <- :')
        entrada=entrada.lower()

        if not entrada:
            print('Você não digitou nada. Tente novamente!')
            input('Aperte qualquer tecla para reiniciar o programa.')
            continue

        if entrada not in permitidos:
            print('Ataque não válido. Tente novamente!')
            input('Aperte qualquer tecla para reiniciar o programa.')
            continue

        print('Computador escolhendo..')
        time.sleep(2)
        computador=escolha_computador()


        print(f'Sua escolha: {entrada.upper()}')
        print(f'Escolha da máquina: {computador.upper()}')

        analise=verificar_vencedor(entrada, computador)

        print(f'Resultado: {analise}')


        continuar=input('Deseja continuar no jogo? [sim/nao]')

        if continuar.lower() == 'nao':
            print('Programa encerrado. Até breve!')
            break
            




if __name__ == '__main__':
    main()