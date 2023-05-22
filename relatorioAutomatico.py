#!/usr/bin/env python
# coding: utf-8

# In[227]:


# passo 0) importando as bibliotecas
import pyautogui
import time
import pyperclip


# In[228]:


# passo 1) Abrir um navegador de internet 

pyautogui.PAUSE = 3
pyautogui.hotkey('ctrl', 't')


# In[229]:


# passo 2) Copiar o link do Google Drive da base de dados
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing"
pyperclip.copy(link)


# In[230]:


# passo 3) Entrar no Google Drive onde está a base
# de dados
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)


# In[231]:


# passo 4) Abrir pasta Aula 1 do Google Drive
pyautogui.click(430, 388, clicks=2)
pyautogui.click(434, 541, clicks=2)

# passo 5) Baixar planilha Vendas – Dez.xlsx
time.sleep(2)
pyautogui.click(96, 141)
pyautogui.click(207, 493)
pyautogui.click(559, 508)
pyautogui.click(756, 544)
pyautogui.click(1028, 561)


# In[232]:


# passo 6) importando a base de dados
import pandas as pd
df = pd.read_excel(r"C:\Users\bruna\OneDrive\Documentos\Vendas - Dez.xlsx")

# passo 7) calcular faturamento (coluna valor final)
faturamento = df['Valor Final'].sum()
# passo 8) calcular quanidade vendida (coluna quantidade)
quantidade = df['Quantidade'].sum()


# In[233]:


# passo 9) criar um relatório via e-mail
    # - abrir o gmail;
pyautogui.hotkey('ctrl', 't')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
    
    # - clicar em escrever;
time.sleep(2)
pyautogui.click(115, 208)
    
    # - escrever o destinatário;
pyautogui.write('thaliadesign.freela@gmail.com')
pyautogui.press('tab')

    
    # - clicar no campo assunto e escrever o assunto;
pyautogui.press('tab')
assunto = 'Relatório de vendas de ontem'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
    
    # - clicar no campo do corpo e escrever o relatório;
pyautogui.press('tab')
texto = f''' 
Prezados, bom dia.
    
O faturamento de ontem foi de R${faturamento:,.2f}
A quantidade de produtos vendidos foi de {quantidade:,}
    
Atenciosamente,
Bruna Milhomem
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
    
    # - enviar email.
pyautogui.hotkey('ctrl', 'enter')

