# Vetor de nome dos formulários 

#caminho_dir = "~/projetos_ml/presenca_formularios/"

import numpy as np 
nomes_arqs_forms_u_1 = [ 'Compreensão do Perfil da Turma', 'História dos computadores', 'Algoritmo', 'Algoritmos Representação', 'Operadores Aritméticos', 'Operadores Lógicos', 'Estrutura Condicional', 'Estrutura Condicional Aplicações'] 
nomes_arqs_forms_u_2 = [ 'Repetição Condicional', 'Repetição Condicional Aplicações', 'Introdução ao P5JS', 'Mouse teclado e ponto dentro de um retângulo', 'Revisão de Repetição Condicional e Introdução a Laço Contado', 'Repetição Contada'] 
nomes_arqs_forms_u_3 = [ 'Introdução e Manipulação de Vetores','Uso e Exemplos de Vetores'] 

# Colunas abreviadas para a primeira unidade 
colunas_u_1 = ['perfil', 'hist','alg','alg_rep','op_ari','op_log','cond','cond_ap']
colunas_u_2 = [ 'rep','rep_ap','intro_p5js', 'mouse','rep_cont_1','rep_cont_2']
colunas_u_3 = ['vet_1','vet_2']

import pandas as pd 
# obtem as mátriculas de um arquivo orginal do SIGAA
#turma_sigaa = pd.read_csv("../dados/turma_5_2020_6.csv")
#turma_sigaa = pd.read_csv("../dados/turma_4_2020_6.csv")
#turma_sigaa = pd.read_csv("../dados/turma_03_2020_2.csv")
turma_sigaa = pd.read_csv("../dados/turma_02_2021_1.csv")

mats_sigaa = turma_sigaa.iloc[:,0].values

from processa_forms import gera_dados_presenca

# Gera presença para as planilhas da unidade 1
dados_frequencia =  gera_dados_presenca(nomes_arqs_forms_u_1,colunas_u_1,mats_sigaa)
dados_frequencia.head() 

dados_frequencia.to_csv("../saida/froms_u1.csv", index=False)

# Gera presença para as planilhas da unidade 2
#dados_frequencia =  gera_dados_presenca(nomes_arqs_forms_u_2,colunas_u_2,mats_sigaa)
#dados_frequencia.head() 

#dados_frequencia.to_csv("../saida/froms_u2.csv", index=False)

# Gera presença para as planilhas da unidade 3
#dados_frequencia =  gera_dados_presenca(nomes_arqs_forms_u_3,colunas_u_3,mats_sigaa)
#dados_frequencia.head() 

#dados_frequencia.to_csv("../saida/froms_u3.csv", index=False)