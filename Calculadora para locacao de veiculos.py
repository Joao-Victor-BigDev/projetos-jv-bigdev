print('===== Calculador de aluguel de carros #BIG =====')
dias = int(input('Quantos dias o veiculo foi alugado ? '))
km = float(input('Quantos Kms foram rodados ? '))
tdias = dias * 60
tkm = km * 0.15
total = tdias + tkm
print(f'O custo da locacao do veiculo foi de R${total}')
