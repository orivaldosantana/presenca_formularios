def gera_dados_presenca( arq_presenca, caminho_arqs = '../dados/' ): 
    # cira o data frame de saída 
    nome_arq = caminho_arqs  + arq_presenca+".csv"
    dados_in = 0
    try: 
      print(nome_arq)
      dados_in = pd.read_csv(nome_arq )
    except:
      # tenta ler o próximo arquivo
      print("Falha ao ler arquivo!\n") 
    posMat = 0 
    # Torna campos vazios em 0
    dados_in.iloc[:,posMat] = dados_in.iloc[:,posMat].fillna(0)
    # Transforma o tipo do campo matricula em inteiro 
    # Para ficar compativel com o uso de indeces mais a frente 
    dados_in.iloc[:,posMat] = dados_in.iloc[:,posMat].astype(int) 

    #mats_temp = dados_temp.iloc[:,1].values
    mats_temp = dados_in.iloc[:,posMat] 
    
    print("--- Processa forms concluído!!! --- \n") 
    # Calcula a média 
    dados_frequencia = dados_in.iloc[:,1:]
    quantidade_de_colunas = len(dados_frequencia.iloc[0,:].values) 
    print(dados_frequencia.head() ) 
    dados_frequencia["total"] = 0
    dados_frequencia["total"] =  dados_frequencia.sum(axis=1)
    dados_frequencia["total"] = (dados_frequencia["total"] * 10 ) / quantidade_de_colunas 
    print(dados_frequencia.iloc[0,1:].values) 

    dados_frequencia["Matrícula"] = mats_temp  

    return dados_frequencia


# Vetor de nome dos formulários 
nomes_arqs_forms_u = []
colunas_u = []

# Indisces para as unidades 
# 0 - I
# 1 - II
# 2 - III 
indiceU = 0

#caminho_dir = "~/projetos_ml/presenca_formularios/"

import numpy as np 
#nomes_arqs_forms_u.append( [ '2022004012', '2022004019', '2022004026', '2022004028', '2022005003', '2022005005', '2022005010', '2022005012' ] )

# Colunas abreviadas para a primeira unidade 
#colunas_u_1 = ['perfil', 'hist','alg','alg_rep','op_ari','op_log','cond','cond_ap']
#colunas_u.append( [ '2022004012', '2022004019', '2022004026', '2022004028', '2022005003', '2022005005', '2022005010', '2022005012' ])

import pandas as pd 


# obtem as mátriculas de um arquivo orginal do SIGAA
turma_sigaa = pd.read_csv("../dados/turma_02_2022_1.csv")
#turma_sigaa = pd.read_csv("../dados/teste.csv")


mats_sigaa = turma_sigaa.iloc[:,0].values

dados_frequencia_res =  gera_dados_presenca('presenca_u1_t02_2022_2')
print(dados_frequencia_res.head())


presenca_uniao_u = pd.merge(turma_sigaa, dados_frequencia_res, how='left', on='Matrícula')
print(presenca_uniao_u) 

#from processa_forms import gera_dados_presenca

# Gera presença para as planilhas da unidade 3
#dados_frequencia =  gera_dados_presenca(nomes_arqs_forms_u[indiceU],colunas_u[indiceU],mats_sigaa)
#print( dados_frequencia.head()  )

presenca_uniao_u.to_csv("../saida/presenca_u{unidade}.csv".format(unidade=indiceU+1), index=False)