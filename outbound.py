import pandas as pd
import numpy as np


# "COLOCAR NOME DO ARVQUIVO DE CLIENTES"
df1 = pd.read_csv("leads-pipedrive.csv")


# "COLOCAR NOME DO ARQUIVO CSV A SER LIMPADO"
df2 = pd.read_csv("leads-teste.csv")

def cleanOutbound(df1, df2):
        df1.rename(columns={"Pessoa - Organização" : "empresa", 
                                            "Pessoa - E-mail": "email"}, inplace=True)
        df2.columns = [x.lower().replace(" ", "_").replace("ê", "e").replace("/", "_") for x in df2.columns]
        # Construindo outra coluna no dataset de outbound para tentar a exclusao novamente
        df2['domain'] = df2['email'].str.split('@').str[1]
        
        # Adicionando empresas do pipe em uma lista, removendo o que está em branco
        empresas = df1['empresa'].values.tolist()
        empresas = [x for x in empresas if str(x) != 'nan']
        # Criando uma lista com os dominios
        emails = df1['email'].values.tolist()
        emails = [str(x) for x in emails if str(x) != 'nan']
        dominios = []
        for email in emails:
                if "@" in email:
                        dominio = email.split("@")[1]
                        dominios.append(dominio)
                else:
                        continue
        
        # Removendo dominios uplicados
        dominios_list = set(dominios)
        # Remover gmail, hotmail e outlook
        ''' REMOVER DOMÍNIOS COMUNS É OPCIONAL'''
        
#        dominios = [e for e in dominios_list if e not in ('gmail.com', 'hotmail.com', 'yahoo.com.br')]
        ## Limpando o dataset
        # Descobrindo o index das empresas em comum
        comps = []
        indexs = []
        for comp in df2['empresa']:
                if comp in empresas:
                        comps.append(comp)
                        index = df2[df2['empresa'] == comp].index.get_values()
                        indexs.append(index)
        arrays_list = []
        index_list = []
        for index in indexs:
                i = index.tolist()
                arrays_list.append(i)
        for array in arrays_list:
                for index in array:
                        index_list.append(index)
        index_empresas = sorted(set(index_list))
        df2_clean = df2.drop(index_empresas)
        # Repetindo a mesma coisa, mas por dominio
        domains = []
        d_indexs = []
        for domain in df2_clean['domain']:
                if domain in dominios:
                        domains.append(domain)
                        index = df2_clean[df2_clean['domain'] == domain].index.get_values()
                        d_indexs.append(index)
        # Organizando lista para remover do dataset
        d_arrays_list = []
        d_index_list = []
        for d_index in d_indexs:
                i = d_index.tolist()
                d_arrays_list.append(i)
        
        for d_array in d_arrays_list:
                for d_index in d_array:
                        d_index_list.append(d_index)
        d_index_empresas = sorted(set(d_index_list))
        
        df3_clean = df2_clean.drop(d_index_empresas)
        print("Empresas encontradas: {}".format(len(comps)))
        print("Dominios Encontrados: {}".format(len(domains)))
        print("Total de removidos: {}".format(len(comps)+len(domains)))
        df3_clean.to_csv("dataset-clean.csv")
        print("Número de Linhas: {}".format(len(df3_clean)))
        print(len(df3_clean))
        return print("acabou")

cleanOutbound(df1, df2)
