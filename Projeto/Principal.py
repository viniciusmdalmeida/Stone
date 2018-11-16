from Interface import TelaInial
from ExtraçãoDados import *
from BancoDados import *


# Interface
# TelaInial()


#Sem interface
linkBase = 'https://www.receitaws.com.br/v1/cnpj/'
cnpjs = [16501555000157, 14994237000140, 18727053000174, 13966572000171, 12839955000116, 16569357000125, 16575851000100, 12592831000189]
tabelaComp,tabelaQSA = pegarDadosLista(linkBase,cnpjs)

bancoDados = BancoDados()
bancoDados.escreverCompanhias(tabelaComp)
bancoDados.escreverQSA(tabelaQSA)

tabelaComp2= bancoDados.pegarCompanhia()
tabelaQSA2 = bancoDados.pegarQSA()
excel = pd.ExcelWriter('saida_Final.xlsx')
tabelaQSA2 .to_excel(excel,sheet_name='QSA')
tabelaComp2.to_excel(excel,sheet_name='Companhias')
excel.save()