# Receba uma distância e uma quantidade de combustível gasta e exiba o consumo médio do veículo.
dist = int(input('Digite uma distância em km: '))
comb = int(input('Digite a quantidade de combustível gasta nessa distância percorrida em litros: '))

media = dist / comb

print(f'O consumo médio do veículo utilizado é de {media:.2f} km/l.')