import pandas as pd

df = pd.read_csv('../arquivos/salarios.csv')

print(df['Name'])

var = df['nome e salario'] = df['Name'] + ' ' + df['Employee Annual Salary']

df.to_csv('name_salario.csv', header=0)

# #print(dt.head())

# #print(dt.iloc[50:])

#parametro loc: numero da linha, nome da coluna
#var2 = df.loc[20,['name','Employee Annual salary']]

#parametro loc: numero da linha, nome da coluna
#print (df.loc[20,2])