## Função para remover clientes e deals do pipe de listas de outbound
___________________

### Instalações:

- Instalar a última versão do python [Baixar Python](https://www.python.org/downloads/)
- Instalar o Anaconda [Baixar Anaconda](https://www.youtube.com/watch?v=T8wK5loXkXg)

### Padrão dos Arquivos:

1. Padrão do arquivo que contem os dados de deals e clientes (exportados do pipedrive, por exemplo):
    - Nome da coluna 01: "Pessoa - Organização"
    - Nome da coluna 02: "Pessoa - E-mail"    

Exporte os arquivos e deixe os exatamente na mesma pasta deste código.

2. Padrão do arquivo que você deseja limpar (uma lista de emails e empresas de outbound, por exemplo):
    - Deve conter uma coluna "empresa"
    - Deve conter uma coluna "email"


### Para usar a função:

1. Abra o terminal do computador e digite **jupyter notebook**
2. Navegue até a pasta dos arquivos: **outFunc.py**, **clientes.csv**, **lista.csv**
3. Aperte o *+* no canto superior direito e crie um notebook python3
4. Copie todo o código do arquivo **outFunc.py** e cole na primeira linha do jupyter notebook
5. Edite as linhas com **df1 = pd.read_csv("COLOCAR NOME DO ARVQUIVO DE CLIENTES AQUI")** e **df2 = pd.read_csv("COLOCAR NOME DO ARQUIVO CSV A SER LIMPADO AQUI")**
6. Aprente **shift + enter**
7. Na linha seguinte digite exatamente **cleanOutbound(df1, df2)**
8. O csv já deve estar na mesma pasta

>  A qualidade da limpeza, se você vai remover todos os clientes que estão nos arquivo 01 do arquivo 02, depende 100% da qualidade dos dados. 

