#%% Bibliotecas
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

#%% Carregando a base de dados
df = pd.read_parquet('databases/dados_clones.parquet')
df.columns
df.head()

#%% Selecionando as features e o target

df['General Jedi encarregado'].unique()

features = ['Massa(em kilos)', 'Estatura(cm)'] #características
target = 'Status '

x = df[features]
y = df[target]
model = tree.DecisionTreeClassifier()
model.fit(X=x, y=y) #treinando o modelo
# %%

tree.plot_tree(model, feature_names=features, class_names=model.classes_, filled=True, max_depth=3, rounded=True)
plt.show()

# %% Analisando a importância das features
pd.DataFrame(model.feature_importances_, index=features, columns=['Importância'])

# %%
df2 = df.groupby('Status ')[features].mean()
# %%
df2.plot(kind='barh')
# %%
plt.show()
# %%
