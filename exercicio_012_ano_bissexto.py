from datetime import date
data = int(input('Escreva o ano que voce quer saber: Digite 0 se quiser saber o ano atual '))
if data == 0:
    data = date.today().year
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print(f'O ano de {data} é BISSEXTO')
else:
    print(f'O ano de {data} NÃO é BISSEXTO')
