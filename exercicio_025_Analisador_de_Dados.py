media = 0
maior = 0
menor = 0
msgF = ''
maiorn = ''
for a in range(1, 5):
    print(f'-----{a}° pessoa-----')
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').upper()
    media += idade
    if a == 1:
        maior = idade
    if idade < 20 and sexo == 'F':
        menor += 1
        msgF = f'Tem {menor} mulher(es) menor que 20 anos.'
    if idade > maior:
        maior = idade
        maiorn = nome
mediatotal = media / 4
print(f'A media do grupo é: {mediatotal}')
print(f'{maiorn} tem a maior idade que é: {maior} anos')
print(msgF)

