#!/usr/bin/env python
# coding: utf-8

# # Projeto Análise de Dados
# 
# ### A situação:
# 
# Analisando o histórico dos clientes dos últimos anos, você
# percebeu que mais de 26% dos clientes que entraram na
# empresa, cancelaram o contrato.
# 
# A única informação que você tem é um arquivo .csv extraído do
# sistema da empresa (apresentado ao lado).

# In[43]:


import pandas as pd

df = pd.read_csv("telecom_users.csv")
display(df)

df = df.drop(["Unnamed: 0"], axis=1)
display(df)


# In[44]:


print(df.info())


# ### Problemas identificados:
# - Dados faltantes na coluna código;
# - Coluna TotalGasto classificado como object, quando deveria ser tratada como int/float;

# In[45]:


# transformando a coluna TotalGasto em float
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
 # apagando a coluna com valores faltantes (NaN)
df = df.dropna(how='all', axis=1)
 # removendo qualquer linha que tenha item vazio
df = df.dropna()
print(df.info())


# ### Nosso problema é:
# 
# “Alto índice de cancelamento de contratos” O que eu quero:
# 
# “Entender os principais motivos que levam ao
# cancelamento para assim gerar um plano de
# ação”

# In[47]:


display(df['Churn'].value_counts())
display(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))


# In[48]:


import plotly.express as px

for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()
        display(df.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])

