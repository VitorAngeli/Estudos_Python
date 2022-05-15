p = input('Escreva uma frase: ').upper().replace(" ", "")
r = p[::-1]
tamanho = len(p)
true = ''
for c in range(0, tamanho):
    if p == r:
        true = 'É um palíndromo'
    else:
        true = 'Não é um palindromo'
print(f'{p} ao contrario é: {r} \nE esta frase: {true}')



