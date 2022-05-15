from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    ano = date.today().year
    nasc = int(input('Escreva a data de nascimento: '))
    dtnac = ano - nasc
    if dtnac < 18:
        menor += 1
    else:
        maior += 1
print(f'Teve {maior} pessoas maiores de idade e,{menor} menores de idade.')







