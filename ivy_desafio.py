import pandas as ivy

# Config pandas
ivy.set_option('display.max_rows', 500)
ivy.set_option('display.max_columns', 500)
ivy.set_option('display.width', 1000)

df = ivy.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSkBXwor8U8tHA6im456_KY739xM4kEV47rEY_RC1SsPN5N9SaTGPrAJd16XtYhINNue4PwHjAfzu_-/pub?output=csv', dtype=str)

# Substituindo valores e padronizando coluna Sexo
df['sexo'].replace('F', 'Feminino', inplace=True)
df['sexo'].replace('fem', 'Feminino', inplace=True)
df['sexo'].replace('M', 'Masculino', inplace=True)
df['sexo'].replace('masc', 'Masculino', inplace=True)

# Convertendo para float para realizar os cálculos do 3 e 4
df['nota_matematica'] = df['nota_matematica'].str.replace(',', '.', regex=False)
df['nota_portugues'] = df['nota_portugues'].str.replace(',', '.', regex=False)

df['nota_matematica'] = df['nota_matematica'].astype(float)
df['nota_portugues'] = df['nota_portugues'].astype(float)
df['frequencia'] = df['frequencia'].astype(float)

# Criando coluna Media
df['media'] = (df['nota_matematica'] + df['nota_portugues'] + (df['frequencia'] / 10)) / 3
df['media'] = df['media'].round(1)

# Criando coluna Aprovado
df['aprovado'] = df['media'].apply(lambda x: 'Sim' if x >= 7 else 'Não')

df.to_excel('Desafio.xlsx')
print(df)