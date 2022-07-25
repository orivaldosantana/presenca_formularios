def calcula_presenca( arq_presenca, posMat = 0, caminho_arqs = '../dados/' ): 
    # cira o data frame de saída 
    nome_arq = caminho_arqs  + arq_presenca+".csv"
    dados_in = 0
    try: 
      print(nome_arq)
      dados_in = pd.read_csv(nome_arq )
    except:
      # tenta ler o próximo arquivo
      print("Falha ao ler arquivo!\n") 
    # Torna campos vazios em 0
    dados_in.iloc[:,posMat] = dados_in.iloc[:,posMat].fillna(0)
    # Transforma o tipo do campo matricula em inteiro 
    # Para ficar compativel com o uso de indeces mais a frente 
    dados_in.iloc[:,posMat] = dados_in.iloc[:,posMat].astype(int) 

    mats_temp = dados_in.iloc[:,posMat] 
    # Calcula a média 
    dados_frequencia = dados_in.iloc[:,1:]
    quantidade_de_colunas = len(dados_frequencia.iloc[0,:].values) 
    print(dados_frequencia.head() ) 
    dados_frequencia["total"] = 0
    dados_frequencia["total"] =  dados_frequencia.sum(axis=1)
    dados_frequencia["total"] = (dados_frequencia["total"] * 10 ) / quantidade_de_colunas 
    print(dados_frequencia.iloc[0,1:].values) 

    dados_frequencia["Matrícula"] = mats_temp  
    print("--- Cálculo de presença concluído!!! --- \n") 
    return dados_frequencia


# Vetor de nome dos formulários 
# Indisces para as unidades 
# 0 - I
# 1 - II
# 2 - III 
indiceU = 2


import pandas as pd 

# obtem as mátriculas de um arquivo orginal do SIGAA
turma_sigaa = pd.read_csv("../dados/turma_02_2022_1.csv")

mats_sigaa = turma_sigaa.iloc[:,0].values

dados_frequencia_res =  calcula_presenca('presenca_u3_t02_2022_2')
print(dados_frequencia_res.head())

presenca_uniao_u = pd.merge(turma_sigaa, dados_frequencia_res, how='left', on='Matrícula')
print("--- Merge com os dados do SIGAA concluído!!! --- \n") 
print(presenca_uniao_u) 

presenca_uniao_u.to_csv("../saida/presenca_u{unidade}.csv".format(unidade=indiceU+1), index=False)