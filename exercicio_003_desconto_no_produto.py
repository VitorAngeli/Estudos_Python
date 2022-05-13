preco = float(input('Digite o preço do produto: '))
porc = (5 / 100) * preco
res = preco - porc
print(f'O produto que custava R${preco}, na promocão com desconto de 5% vai custar R${res:.2f} ')