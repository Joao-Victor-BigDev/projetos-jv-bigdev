print('===== Veriicador de Lista Vip =====')
lista = ['Joao Victor', 'Thiago', 'Fernando', 'Luana']
nome = str(input('Digite o nome para verificacao na lista vip. ')).strip()
capt = nome.title()
if capt in lista:
    print(f'Seja bem vindo(a) a FESTA ! {nome}')
    entrou = input('O acesso esta liberado !')
else:
    print('O nome nao esta na lista')
    suporte = input('Contate Gabriel-(11) 98869-4447 para ter suporte, ')
