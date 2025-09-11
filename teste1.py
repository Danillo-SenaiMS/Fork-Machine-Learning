# %%

import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

# %%

df = pd.read_excel('databases/dados_frutas.xlsx')
df.head()

# %%

arvore = tree.DecisionTreeClassifier(random_state=42)

# %%

y = df['Fruta']
caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']
x = df[caracteristicas]


# %%

arvore.fit(x, y)

# %%

#Aqui iremos desenhar a árvore de decisão
fig = plt.figure(figsize=(10, 6), dpi=100)
tree.plot_tree(arvore, feature_names=caracteristicas, class_names=arvore.classes_, filled=True)
plt.show()

# %%
