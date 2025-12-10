from validacao import validar
def main():
    print('𝚅𝚊𝚕𝚒𝚍𝚊𝚗𝚍𝚘 𝚌𝚙𝚏...')
    while True:

        entrada=input('Digite o seu cpf:')
        
        if validar(entrada):
            print(f'CPF: {entrada} validada!')

        opcao_continuar=input('Deseja validar outro número: [sim/nao]')
        if opcao_continuar.lower() == 'nao':
            print('Programa encerrado.')
            break



















if __name__=='__main__':
    main()


        
        