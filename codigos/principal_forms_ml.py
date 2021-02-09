import numpy as np 
nomes_arqs_forms = ['Compreensão do Perfil da Turma ML', 'Introdução ao Aprendizado de Máquina', 'Aprendizado de Máquina Exemplos', 'Introdução ML Principais Conceitos', 'Introdução à Regressão Linear', 'Multilayer Perceptron Parte 1', 'Multilayer Perceptron Parte 2', 'Support Vector Machine' ] 

colunas = ['perfil', 'introML','introExp','introConc','regre','mlp1','mlp2','svm']

import pandas as pd 
turma_sigaa = pd.read_csv("../dados/turma_ml_2020_2.csv") 


mats_sigaa = turma_sigaa.iloc[:,0].values

from processa_forms import gera_dados_presenca


dados_frequencia = gera_dados_presenca(nomes_arqs_forms, colunas, mats_sigaa)
dados_frequencia.head() 

dados_frequencia.to_csv("../saida/froms_ml.csv", index=False)



