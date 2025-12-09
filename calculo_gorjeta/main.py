from ferramentas import calcular_gorjeta, valor_total

def main():
    print(" -- 𝙲𝚊𝚕𝚌𝚞𝚕𝚊𝚍𝚘𝚛𝚊 𝚍𝚎 𝚐𝚘𝚛𝚓𝚎𝚝𝚊 -- ")

    try:
        while True:
            conta=float(input('Digite o valor da conta:'))
            if conta < 0:
                print('A conta deve ser maior que 0$ para um cálculo')
                continue

            porcent=int(input('Digite a porcentagem de gorjeta:'))
            if porcent < 0 and porcent > 100:
                print('A porcentagem precisar estar entre 1 e 100')
                continue

            resultado=calcular_gorjeta(conta, porcent)
            valor_com_gorjeta=valor_total(conta, resultado)
            print(f'Valor da gorjeta: R${resultado:.2f} ')
            print(f'Total a pagar: R${valor_com_gorjeta:.2f}')

            opcao=input('Deseja continuar? [sim/nao]')
            if opcao.lower() == 'nao':
                break

    except ValueError:
        print('Digite apenas números.')



if __name__ == "__main__":
    main()


