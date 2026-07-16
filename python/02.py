# %%

import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

# %%
df = pd.read_excel('databases/dados_cerveja.xlsx')

# %%

df.columns


# %%

features = ['temperatura', 'copo', 'espuma', 'cor'] #características
target = 'classe'

x = df[features]
y = df[target]

# Transformando variáveis categóricas em numéricas ( variáveis dummies)
x = x.replace({
    'mud': 1,
    'pint': 2,
    'sim': 1,
    'não': 0,
    'clara': 0,
    'escura':1
})

model = tree.DecisionTreeClassifier()
model.fit(X=x, y=y) #treinando o modelo
# %%

tree.plot_tree(model, feature_names=features, class_names=model.classes_, filled=True)
plt.show()
# %%
