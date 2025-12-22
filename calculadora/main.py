from ferramentas import calcular
import os

while True:
    os.system('cls')
    print('𝘾𝘼𝙇𝘾𝙐𝙇𝘼𝘿𝙊𝙍𝘼')

    try:

        
        num1=int(input('Digite o primeiro número:'))
        operacao=input('Digite a operação desejada: [+, -, *, /] :')
        num2=int(input('Digite o segundo número:'))

        
        resultado=calcular(num1, num2, operacao)
        os.system('cls')
        print('-----------------Cálculo------------------')
        print(f'{num1} {operacao} {num2} = {resultado}')

        reiniciar=input('Deseja continuar?[sim/nao]:')
        if reiniciar.lower() == 'nao':
            os.system('cls')
            print('Calculadora encerrada. Até breve!')
            break


    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
        input('Aperte qualquer tecla para reinciar')
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')
        input('Aperte qualquer tecla para reinciar')





