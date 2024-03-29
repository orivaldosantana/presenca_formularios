# Módulo 

def teste():
    print("Teste!")

import pandas as pd 

def gera_dados_presenca( arqs_forms, colunas_u, mats, caminho_arqs = '../dados/' ): 
    # cira o data frame de saída 
    df = pd.DataFrame(columns=colunas_u, index=mats )
    dados_frequencia = df.fillna(0) 
    # posição (coluna) da mátricula no arquivo  
    posMat = 2
    # Lê todos os csvs dos forms de aula  
    for n in range(0, len(arqs_forms), 1):
        nome_arq = caminho_arqs +"'"+ arqs_forms[n]+"'.csv"
        try:
            print(nome_arq)
            dados_temp  = pd.read_csv(nome_arq)
        except:
            # tenta ler o próximo arquivo
            print("Falha ao ler arquivo!\n") 
            continue 

        # Torna campos vazios em 0
        dados_temp.iloc[:,posMat] = dados_temp.iloc[:,posMat].fillna(0)
        # Transforma o tipo do campo matricula em inteiro 
        # Para ficar compativel com o uso de indeces mais a frente 
        dados_temp.iloc[:,posMat] = dados_temp.iloc[:,posMat].astype(int) 

        #mats_temp = dados_temp.iloc[:,1].values
        mats_temp = dados_temp.iloc[:,posMat].values    
        

        for i in range(mats.size):
            for j in range(mats_temp.size):
                if  (mats[i]==mats_temp[j]):
                    dados_frequencia[ colunas_u[n] ][mats[i]] = 1
                    #print(". "+colunas_u_1[n])
        print("Ok - Leitura realizada com sucesso!\n")
    print("--- Processa forms concluído!!! --- \n") 
    # Calcula a média 
    dados_frequencia["total"] = 0
    dados_frequencia["total"] =  dados_frequencia.sum(axis=1)
    dados_frequencia["total"] = (dados_frequencia["total"] * 10 ) / len(arqs_forms)

    dados_frequencia["matricula"] = mats 

    return dados_frequencia