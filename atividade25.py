# os valores são determinados pelo usuário

capital = int(input('Insira o valor do capital: '))
juros = int(input('Insira a taxa de juros "em porcentagem" por mês: '))
tempo = int(input('Insira o tempo em meses: '))

# fórmula para calcular os juros simples

juros_simples = capital * (juros / 100) * tempo

# printa a resposta

print(f'O valor dos juros acumulados é {juros_simples:.2f}')