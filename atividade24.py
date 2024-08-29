# o valor é determinado pelo usuário

num1 = int(input('Insira um número para aplicar desconto: '))

# fórmula básica de multiplicação para determinar a porcentagem 

desconto = num1 - 10%num1

# printa a resposta

print(f'O valor com desconto é {desconto:.2f}')