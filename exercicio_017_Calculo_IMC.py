peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))
imc = peso / (altura * altura)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
