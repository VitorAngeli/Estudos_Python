seg1 = int(input('Primeiro Segmento: '))
seg2 = int(input('Segundo Segmento: '))
seg3 = int(input('Terceiro Segmento: '))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print(f'Os segmentos a cima podem formar um triangulo ', end='')
    if seg1 == seg2 and seg1 == seg3 and seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('ISÓSCELES')
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print('ESCALENO')
else:
    print('Os segmentos a cima NÃO podem se tornar um TRIANGULO')




