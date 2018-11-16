import MySQLdb
import pandas as pd
#Instalar pip install MySQL-python

class BancoDados:
    host = 'sql10.freemysqlhosting.net'
    database = 'sql10265799'
    user = 'sql10265799'
    password = 'dj8PKJ3t3x'
    port = 3306

    def __init__(self):
        try:
            self.criarTabelas()
        except:
            pass

    def conectar(self):
        self.con = MySQLdb.connect(self.host, self.user, self.password)
        self.con.select_db(self.database)
        self.cursor = self.con.cursor()

    def criarTabelas(self):
        self.conectar()
        try:
            sql = "CREATE TABLE companhias (" \
                  " cnpj VARCHAR(20) NOT NULL," \
                  " nome VARCHAR(100) NOT NULL," \
                  " atividade_principal VARCHAR(100)," \
                  " data_de_abertura DATETIME ," \
                  " capital_social DOUBLE," \
                  " PRIMARY KEY (cnpj));"
            self.cursor.execute(sql)

            sql = "CREATE TABLE QSA (" \
                  " nome VARCHAR(100)," \
                  " qual VARCHAR(100) NOT NULL," \
                  " cnpj VARCHAR(20));"
            self.cursor.execute(sql)
            self.con.close()
        except Exception as  e:
            print("Error",e)
            self.con.close()

    def inserirCompanhia(self,linha):
        self.conectar()
        try:
            sql = "INSERT INTO companhias (cnpj,nome,atividade_principal,data_de_abertura,capital_social)  VALUES (%s,%s,%s,%s,%s)"
            val = (linha['cnpj'], linha['nome'], linha['atividade_principal'], linha['abertura'], linha['capital_social'])
            self.cursor.execute(sql, val)
            self.con.commit()
        except  Exception as e:
            print('error:', e)
        else:
            self.con.close()

    def inserirCompanhia2(self,linha):
        self.conectar()
        try:
            sql = "INSERT INTO companhias (cnpj,nome,atividade_principal,abertura,capital_social,bairro,cep,"
            "complemento,numero,logradouro,municipio,data_situacao,natureza_juridica,telefone,tipo,uf,email,fantasia)" \
            "  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (
                str(linha['cnpj']), str(linha['nome']), str(linha['atividade_principal']), str(linha['abertura']),
                str(linha['capital_social']),
                str(linha['bairro']), str(linha['cep']), str(linha['complemento']), str(linha['numero']),
                str(linha['logradouro']), str(linha['municipio']),
                str(linha['data_situacao']), str(linha['natureza_juridica']), str(linha['telefone']),
                str(linha['tipo']), str(linha['uf']), str(linha['email']), str(linha['fantasia']))
            self.cursor.execute(sql, val)
            self.con.commit()
        except  Exception as e:
            print('error:', e)
        else:
            self.con.close()

    def inserirQSA(self,linha):
        self.conectar()
        try:
            sql = "INSERT INTO QSA (nome,qual,cnpj)  VALUES (%s,%s,%s)"
            val = (linha['nome'], linha['qual'], linha['CNPJ'])
            print(val)
            self.cursor.execute(sql, val)
            self.con.commit()
        except  Exception as e:
            print('error:', e)
        else:
            self.con.close()

    def pegarCompanhia(self):
        self.conectar()
        try:
            tabela = pd.read_sql('SELECT * FROM companhias', con=self.con)
            self.con.close()
            return tabela
        except:
            self.con.close()


    def pegarQSA(self):
        self.conectar()
        try:
            tabela = pd.read_sql('SELECT * FROM QSA', con=self.con)
            self.con.close()
            return tabela
        except:
            self.con.close()
        return tabela

    def escreverCompanhias(self,tabela):
        for n_linha in range(len(tabela)):
            linha = tabela.iloc[n_linha]
            self.inserirCompanhia(linha)

    def escreverQSA(self,tabela):
        for n_linha in range(len(tabela)):
            linha = tabela.iloc[n_linha]
            self.inserirQSA(linha)