import requests
import pandas as pd
import time
from datetime import datetime
from tkinter import END

print = print

def Criando_links(linkBase, cnpjs):
    global print
    links = []
    for cnpj in cnpjs:
        links.append(linkBase + str(cnpj))
    return links

def retirarDados(json):
    global print
    chaves = json.keys()
    removeItens = ['qsa', 'atividades_secundarias', 'billing', 'extra']
    jsonQSA = json['qsa']
    for item in removeItens:
        if item in chaves:
            del json[item]
    json['atividade_principal_code'] = json['atividade_principal'][0]['code']
    json['atividade_principal'] = json['atividade_principal'][0]['text']
    # Convertendo string abertura para data
    json['abertura'] = datetime.strptime(json['abertura'], '%d/%M/%Y')
    print(json['nome'])
    # Corvertendo string data_situacao para data
    #     if json['data_situacao']
    return json, jsonQSA

def pegarDadosLink(link,cnpj):
    global print
    print('CNPJ='+ str(cnpj))
    site = requests.get(link)
    json = site.json()
    if json['status'] == "ERROR":
        raise Exception("CNPJ Invalido")
    jsonEmp, jsonQSA = retirarDados(json)
    #     print("####",json,"#####",jsonQSA)
    return jsonEmp, jsonQSA


def cria_tabelaQSA(tabelaAtual, qsa, cnpj):
    global print
    tabelaNova = pd.DataFrame(qsa)
    tabelaNova['CNPJ'] = [cnpj] * len(tabelaNova)
    tabelaNova = pd.concat([tabelaAtual, tabelaNova])
    return tabelaNova


def pegarDadosLista(linkBase,cnpjs, tempoConsulta=20,interface=False,textLabel=None):
    global print
    def printText(text,end="\n"):
        textLabel.insert(END,str(text)+end)

    if interface:
        print = printText

    dicionario = {}
    dicinoarioQSA = {}
    tabelaQSA = pd.DataFrame()
    links = Criando_links(linkBase, cnpjs)
    # print(links)
    for i in range(len(links)):
        link = links[i]
        print("{}/{}".format(i+1,len(links)),end=':')
        try:
            dados, qsa = pegarDadosLink(link,cnpjs[i])
            dicionario[cnpjs[i]] = dados
            tabelaQSA = cria_tabelaQSA(tabelaQSA, qsa, cnpjs[i])
        except Exception as e:
            print('Error: '+str(e))
            continue
        finally:
            time.sleep(tempoConsulta)

    tabelaCompa = pd.DataFrame(dicionario)
    tabelaCompa = tabelaCompa.transpose()
    return tabelaCompa, tabelaQSA

