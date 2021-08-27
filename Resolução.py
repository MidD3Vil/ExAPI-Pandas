# Importar a Integração do python com o Excel
import pandas as pd


# Importar e conectar com a Integração do python com o SMS (Twilio)
from twilio.rest import Client
# Seu SID do Twilio:
account_sid = "********************"
# Seu token do Twilio
auth_token = "*********************"
client = Client(account_sid, auth_token)


# PRONTO! CONECTADO, AGORA PODEMOS COMEÇAR A ANÁLISE DO EXCEL

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada mês na lista de meses(lista_meses)...
for mes in lista_meses:

    # Mostre o mês / leia o (mês).xlsx --> No caso o mês mudará de acordo com o parâmetro "for"
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Se algum(any) valor da tabela Vendas for maior ou igual a 55k...
    if (tabela_vendas['Vendas'] >= 55000).any():

        # Para localizar onde está o vendor e as vendas do mesmo...
        # loc[linha, coluna] --> linha = tabela_vendas['Vendas'] >= 55000 && coluna = Vendedor/Vendas
        # .values[0] --> Para especificar apenas o valor, já que o Pandas transforma a informação em uma tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendas'].values[0]

        # PRONTO! AGORA SÓ NOS RESTA ENVIAR O EMAIL
        message = client.messages.create(
            to="+5511*********",
            from_="+19478885697",
            body=f'No mês {mes} o funcionário(a) {vendedor} atingiu a meta!\nValor das vendas: R$ {vendas},00')

        print('Mensagem enviada com sucesso!')
