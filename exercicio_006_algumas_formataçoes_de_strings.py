nome = input('Digite seu nome: ').strip()
print(f'{nome.upper()} \n{nome.lower()} \n{len(nome) - nome.count(" ")} \n{nome.find(" ")}')