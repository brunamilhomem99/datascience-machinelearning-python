#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 1) Pesquisar os valores da commodities;
from selenium import webdriver
import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
display(tabela)

nav = webdriver.Chrome()
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    produto = produto.replace('á', 'a'). replace('ã', 'a').replace('é', 'e').replace('ú', 'u').replace('ó', 'o').replace('ç', 'c')
    link = f"https://www.melhorcambio.com/{produto.lower()}-hoje"
    print(link)
    nav.get(link)
    preco = nav.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
    preco = preco.replace('.', '').replace(',', '.')
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    display(tabela)

nav.quit()
tabela["Comprar"] = tabela["Preço Ideal"] > tabela["Preço Atual"]
tabela.to_excel("commodities_atualizado.xlsx", index=False)


# In[ ]:




