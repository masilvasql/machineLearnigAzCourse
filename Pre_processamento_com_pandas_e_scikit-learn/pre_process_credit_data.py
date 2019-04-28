# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:44:30 2019

@author: marcelo abrão da silva
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
descritor = base.describe()  #mostra informações sobre a base

idadeNegativa = base.loc[base['age'] < 0] #encontra os dados inconsistentes

#apagar coluna (não é interessante)
#1 = coluna inteira
#inplace = só roda o comando na prórpia base de dados sem retorno
base.drop('age', 1, inplace=True) 

#apagar somente os registros com problema
#não é interessante também, devido a deletar alguns dados históricos
base.drop(base[base.age < 0].index, inplace = True)

#preencher os valores manualmente
#preencher os valores com a média
#mais indicada e eficiente
mediaDadosBase = base.mean() # comando traz a média
mediaIdade = base['age'].mean() #apenas a média de idades
mediaIdadeCorreta = base['age'][base.age > 0].mean()
base.loc[base.age < 0 , 'age'] = 40.92

valoresNulos = pd.isnull(base['age']) #recurso do python
valloresNulosPandas = base.loc[pd.isnull(base['age'])]

#dividindo a base entre atributos previsores e atributos de classe
#iloc usado pra fazer a divisão da base
# : (dois pontos) = PEGA todas as linhas
# 1:4, separa a base do atributo 1 ao 4
# do income até o loan, 1:4 (o último valor definido não entra na variável)
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

#tratando valores nulos
# imputer vai auxiliar para preencher valores faltantes
from sklearn.preprocessing import Imputer
#ctrl + i = mostra informações da classe
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])

#Escalonamento de atributos
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()