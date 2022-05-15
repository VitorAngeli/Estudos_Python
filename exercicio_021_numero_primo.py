#s = 0
#for c in range(1, 7):
#    n = int(input('Escreva um numero: '))
#    if n % 2 == 0:
#        s += n
#print(s)

#t = int(input('Escreva o termo: '))
#r = int(input('Escreva a razão: '))
#pa = t + (10 - 1) * r
#for c in range(t, pa + r, r):
#    print(c)

n = int(input('Escreva um Numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}',end=' ')
print(f'\n \033[0mNUmero de divisões: {tot}')
if tot == 2:
    print('\n \033[0mÉ um numero primo')
else:
    print('\n \033[0mNão é um numero primo')

