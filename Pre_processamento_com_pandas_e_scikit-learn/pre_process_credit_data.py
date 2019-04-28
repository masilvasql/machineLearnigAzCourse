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
