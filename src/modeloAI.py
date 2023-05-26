#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("advertising.csv")
display(df)
print(df.info())

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), cmap='Wistia', annot=True)
plt.show()


# In[19]:


# modelagem + algoritmos
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np

x = df.drop('Vendas', axis=1)
y = df['Vendas']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# treino AI
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
rf_reg = RandomForestRegressor()
rf_reg.fit(x_train, y_train)

# teste AI
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

# verificando o resultado com indicadores r2 e rsme
r2_lin = metrics.r2_score(y_test, test_pred_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_test, test_pred_lin))
print(f'R² da Regressão Linear: {r2_lin}')
print(f'RMSE da Regressão linear: {rmse_lin}')
r2_rf = metrics.r2_score(y_test, test_pred_rf)
rmse_rf = np.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))
print(f'R² do Random Forest: {r2_rf}')
print(f'RMSE do Random Forest: {rmse_rf}')


# In[20]:


# resultados em gráfico
reslts = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
plt.figure(figsize=(5, 5))
sns.barplot(x=reslts.index, y=reslts[0])
plt.show()

