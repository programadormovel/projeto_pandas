import pandas as pd

# cidades = pd.Series(['Itapevi', 'Rio de Janeiro', 'Belo Horizonte', \
#     'Santo André', 'Itaquaquecetuba', 'Carapicuíba', 'Barueri', 'Itu', \
#     'São Paulo'])

# populacao = pd.Series([260000, 6700000, 2700000, 720000, 375000,
#                        400000, 276000, 175000, 12000000])

# data_frame = pd.DataFrame({'Cidade': cidades, 'População': populacao})

# print(data_frame)

# populacao_cidades = dict(zip(cidades, populacao))

# print(populacao_cidades)

# print(type(populacao_cidades))

# print(populacao_cidades['Itu'])
# del populacao_cidades['Carapicuíba']
# print('Belo Horizonte' in populacao_cidades)
# #data_frame.to_csv("C:\\treino\\projeto_pandas\\data_frame.csv")
# data_frame.to_csv("data_frame.csv")

cidades_populacao = pd.read_csv("data_frame.csv", index_col = 0)

print(cidades_populacao)
print(cidades_populacao.info())
print(cidades_populacao.columns)
print(cidades_populacao.index)
print(cidades_populacao.head(3))
print(cidades_populacao.describe())
print(cidades_populacao.tail())

