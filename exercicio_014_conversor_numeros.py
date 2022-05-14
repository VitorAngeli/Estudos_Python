numero = int(input('Digite um numero inteiro: '))
opcao = 0
while opcao != 3:
    print('[ 1 ] converter para BINÁRIO')
    print('[ 2 ] converter para OCTAL')
    print('[ 3 ] converter para HEXADECIMAL')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('--' * 20)
        print(f'O numero BINÁRIO é {bin(numero)}')
        print('--' * 20)
    elif opcao ==2:
        print('--' * 20)
        print(f'O numero OCTAL é {oct(numero)}')
        print('--' * 20)
    else:
        print('--' * 20)
        print(f'O numero HEXADECIMAL é {hex(numero)}')
        print('--' * 20)