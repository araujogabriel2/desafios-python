
def calcular(num1, num2, operacao):
    operacoes={
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "*": lambda:num1 * num2,
        "/": lambda: num1 / num2
    }
    if operacao in operacoes:
        return operacoes[operacao]()
    else:
        return 'Operação inválida. Digite apenas as operações listadas -> [+, -, *, /]'

  

 
    
