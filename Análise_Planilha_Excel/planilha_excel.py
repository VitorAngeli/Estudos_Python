import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC331c08131071197c3c8cdea40a5ae22f"
# Your Auth Token from twilio.com/console
auth_token  = "658e6ce1a98badc5aab012f96731bdda"

client = Client(account_sid, auth_token)

# Abri os arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5511991667801",
            from_="+16204624370",
            body=f'No mês de {mes}, o vendedor: {vendedor} bateu a meta, com {vendas} de vendas!')
        print(message.sid)


# para cada arquivo:

# verificar se algum valor na coluna vendas é maior que 55.000

# se for maior, mandar um sms, com o nome do vendedor, mes e valor

