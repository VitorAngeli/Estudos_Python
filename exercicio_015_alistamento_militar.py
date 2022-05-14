from datetime import date
ano = int(input('Digite o ano de nascimento: '))
alistamento = date.today().year - ano
maioridade = 18
if alistamento < maioridade:
    print(f'Quem nasceu em {ano} tem {alistamento} anos em {date.today().year} \nAinda faltam {maioridade - alistamento} anos para o alistamento.')
    print(f'Seu alistamento será em {ano + maioridade}')
elif alistamento > maioridade:
    print(f'Quem nasceu em {ano} tem {alistamento} anos em {date.today().year} \nVoce já deveria ter se alistado há {alistamento - maioridade} anos.')
    print(f'Seu alistamento foi em {ano + maioridade}')
else:
    print(f'Quem nasceu em {ano} tem {alistamento} anos em {date.today().year} \nVoce tem que se alistar IMEDIATAMENTE!')

