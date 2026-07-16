#%% Importando Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# %% Carregando Dataset Iris
iris = datasets.load_iris()
iris.keys()

# %%
iris["target_names"]

# %%
x = iris['data'][:, 3:]  # petal width
y = (iris['target'] == 2).astype(np.int64)  # 1 if Iris-Virginica, else 0

# %%

log_reg = LogisticRegression()
log_reg.fit(x, y)

# %% Gráfico da Regressão Logística

fig, ax = plt.subplots(figsize=(15,8))
x_new = np.linspace(0, 3, 1000).reshape(-1,1)
y_proba = log_reg.predict_proba(x_new)
plt.plot(x_new, y_proba[:,1])


# %% Treinando Modelo SoftMax

x = iris['data'][:, (2,3)]
y = iris['target']

# %%
softmax_reg = LogisticRegression(
    solver='lbfgs',
    )
softmax_reg.fit(x,y)
