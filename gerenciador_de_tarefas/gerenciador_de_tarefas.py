import os 
lista_tarefa=[]


while True:
    os.system('cls')
    print('𝔾𝕖𝕣𝕖𝕟𝕔𝕚𝕒𝕕𝕠𝕣 𝕕𝕖 𝕥𝕒𝕣𝕖𝕗𝕒𝕤')
    print('1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefa\n4. Sair')

    try:

        entrada_comandos=int(input('Digite uma opção:'))

        if entrada_comandos == 1:
            os.system('cls')
            tarefa=input('Digite a tarefa a ser adicionada:')
            lista_tarefa.append(tarefa)
            print(f'Tarefa "{tarefa}" adicionada!')

        elif entrada_comandos ==2:

            if not lista_tarefa:
                print('Não há tarefas a serem exibidas!')
            
            else:
                os.system('cls')
                print('Tarefas:')
                for i, tarefa in enumerate(lista_tarefa):
                    print(f'{i+1}. {tarefa}')

        elif entrada_comandos ==3:

            if not lista_tarefa:
                print('Não há tarefas a serem removidas!')
            
            else:
                os.system('cls')

                for i, tarefa in enumerate(lista_tarefa):
                    print(f'{i+1}. {tarefa}')
                remover=int(input('Digite o número da tarefa a ser removida:'))
                indice_remover=remover - 1

                if 0 <= indice_remover < len(lista_tarefa) :
                    tarefa_removida=lista_tarefa.pop(indice_remover)
                    print(f'Tarefa "{tarefa_removida}" removida com sucesso!')

                else:
                    print(' Erro: Esse índice não existe na lista.')
                
        
        elif entrada_comandos == 4:
            print('Saindo do gerenciador de tarefas. Até mais!')
            break

        else:
            print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
        
        input('Aperte qualquer tecla para voltar ao meunu principal.')


    except ValueError:
        print('Erro: Entrada inválida! Digite um número')
        input('Aperte qualquer tecla para voltar ao meunu principal.')

 
