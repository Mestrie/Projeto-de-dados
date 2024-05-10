#Importando Bibliotecas
import pandas as pd
import plotly.express as px
#Visualizar a base de dados
tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
print(tabela)
#Corrigindo a base de dados
print(tabela.info())
#Excluindo as linhas que têm valores vazios
tabela = tabela.dropna()
print(tabela.info())
#Análise inicial dos cancelamentos
#Quantas pessoas cancelaram e quantas não cancelaram
print(tabela["cancelou"].value_counts())
# em %
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
#Análise das causas dos cancelamentos
# criar o grafico
color_map = {"Sim": "green", "Não": "red"}

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", color_discrete_map=color_map)
    # exibir o grafico
    grafico.show()
# clientes do contrato mensal TODOS cancelam
    # ofercer desconto nos planos anuais e trimestrais
# clientes que ligam mais do que 4 vezes para o call center, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
# clientes que atrasaram mais de 20 dias, cancelaram
    # política de resolver atrasos em até 10 dias (equipe financeira)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts())
# em percentual
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
