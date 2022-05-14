import random as rd
opcao = int(input('Digite um numero: '))
lista = [1, 2, 3, 4, 5]
escolhido = rd.choice(lista)
if escolhido == opcao:
    print('Parabens, voce ganhou...')
elif opcao > 5:
    print('Digite um numero de 1 até 5 para jogar.')
else:
    print(f'Desculpe...Eu pensei no {escolhido}!')
