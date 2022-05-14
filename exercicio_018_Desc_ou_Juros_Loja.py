preco = float(input('Digite o valor do produto: '))
print('[1] - á vista dinheiro/cheque')
print('[2] - á vista cartão')
print('[3] - 2x no cartão')
print('[4] - 3x ou mais no cartão')
opcao = int(input('Escolha uma das opções: '))
if opcao == 1:
    porc = (10 / 100) * preco
    desc = preco - porc
    print(f'Como o pagamento foi a vista voce terá um desconto de 10%, então o produto sairá por R${desc:.2f}')
elif opcao == 2:
    porc2 = (5 / 100) * preco
    desc2 = preco - porc2
    print(f'Como o pagamento foi a vista voce terá um desconto de 5%, então o produto sairá por R${desc2:.2f}')
elif opcao == 3:
    print(f'O valor do produto é: R${preco}')
elif opcao == 4:
    porc3 = (20 / 100) * preco
    juros = preco + porc3
    print(f'Como o pagamento foi no cartão voce terá um acrescimo de 20%, então o produto sairá por R${juros:.2f}')
