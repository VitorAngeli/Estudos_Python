casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anos = int(input('Quantos anos: '))
mensal = casa / (anos * 12)
porc = salario * 30 / 100
if mensal <= porc:
    print(f'O seu salário representa mais que 30% da mensalidade. \nAPROVADO!')
else:
    print(f'Para finanaciar uma casa de R${mensal} reais mensais, a mensalidade não pode ser maior que 30% da sua renda mensal. \nNEGADO!')

