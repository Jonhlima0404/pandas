import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('iris.csv')
# Exibir as primeiras linhas do DataFrame
print(df.head())

# Exibir informações sobre o DataFrame
print(df.info())

# Calcular estatísticas descritivas
print(df.describe())

# Verificar valores nulos
print(df.isnull().sum())

# Gerar um gráfico de dispersão entre duas colunas
df.plot(x='sepal_length', y='sepal_width', kind='scatter')
