from random import randint #Randint -> Faz uma randomização de um numero inteiro
from time import sleep
print('Suas opções: \n'
      '[0] - Pedra\n'
      '[1] - Papel\n'
      '[2] - Tesoura')
opcao = int(input('Qual sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
lista = ('pedra', 'papel', 'tesoura')
escolha = randint(0, 2)
print(f'O Adversário escolheu: {lista[escolha]}\nE voce escolheu: {lista[opcao]}')
if escolha == 0 and opcao == 1:
    print(f'Parabens voce venceu')
elif escolha == 1 and opcao == 2:
    print(f'Parabens voce venceu')
elif escolha == 2 and opcao == 0:
    print(f'Parabens voce venceu')
elif escolha == opcao:
    print('EMPATE')
else:
    print(f'Voce perdeu...')