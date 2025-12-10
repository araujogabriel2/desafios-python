

# validando
def validar(cpf):
    cpf_limpo= cpf.replace('.', '').replace('-','')
     
    if not cpf_limpo.isdigit():
        print('ERROR: Digite apenas números!')
        return False
    
    if len(cpf_limpo) != 11:
        print('ERROR: O cpf deve conter 11 números!')
        return False
    
    return True

        
            




    