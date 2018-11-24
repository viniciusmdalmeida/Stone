import mysql.connector
import pandas as pd
#Instalar pip install MySQL-python

class conectar:
    def __enter__(self):
        host = 'db4free.net'
        database = 'desafiostone'
        user = 'desafiostone'
        password = 'stoneQ123'
        port = 3306

        # Conectando ao banco
        self.con = mysql.connector.connect(user=user,
                                      password=password,
                                      host=host,
                                      database=database)
        return self.con

    def __exit__(self, type, value, traceback):
        self.con.close()

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

    def tabelaExiste(self):
        return True

    def criarTabelas(self):
        with conectar() as con:
            cursor = con.cursor()
            sql = "CREATE TABLE companhias (" \
              " cnpj VARCHAR(20) NOT NULL," \
              " nome VARCHAR(100) NOT NULL," \
              " atividade_principal VARCHAR(100)," \
              " data_de_abertura DATETIME ," \
              " capital_social DOUBLE," \
              " bairro VARCHAR(100)," \
              " cep VARCHAR(50)," \
              " complemento VARCHAR(100)," \
              " numero INTEGER," \
              " logradouro VARCHAR(100)," \
              " municipio VARCHAR(100)," \
              " data_situacao DATETIME ," \
              " natureza_juridica VARCHAR(100)," \
              " telefone VARCHAR(20)," \
              " tipo VARCHAR(20)," \
              " uf VARCHAR(20)," \
              " email VARCHAR(100),"\
              " fantasia VARCHAR(100)," \
              " PRIMARY KEY (cnpj));"
            cursor.execute(sql)

            sql = "CREATE TABLE QSA (" \
                  " nome VARCHAR(100)," \
                  " qual VARCHAR(100) NOT NULL," \
                  " cnpj VARCHAR(20));"
            cursor.execute(sql)
            con.close()


    def inserirCompanhia(self,linha):
        with conectar() as con:
            cursor = con.cursor()
            sql = "INSERT INTO companhias (cnpj,nome,atividade_principal,data_de_abertura,capital_social)  VALUES (%s,%s,%s,%s,%s)"
            val = (linha['cnpj'], linha['nome'], linha['atividade_principal'], linha['abertura'], linha['capital_social'])
            cursor.execute(sql, val)
            con.commit()

    def inserirCompanhia2(self,linha):
        with conectar() as con:
            cursor = con.cursor()
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
            cursor.execute(sql, val)
            con.commit()

    def inserirQSA(self,linha):
        with conectar() as con:
            cursor = con.cursor()
            sql = "INSERT INTO QSA (nome,qual,cnpj)  VALUES (%s,%s,%s)"
            val = (linha['nome'], linha['qual'], str(linha['CNPJ']))
            print(val)
            cursor.execute(sql, val)
            con.commit()

    def pegarCompanhia(self):
        with conectar() as con:
            tabela = pd.read_sql('SELECT * FROM companhias', con=con)
            con.close()
            return tabela


    def pegarQSA(self):
        with conectar() as con:
            tabela = pd.read_sql('SELECT * FROM QSA', con=con)
            con.close()
            return tabela

    def escreverCompanhias(self,tabela):
        for n_linha in range(len(tabela)):
            linha = tabela.iloc[n_linha]
            self.inserirCompanhia(linha)

    def escreverQSA(self,tabela):
        for n_linha in range(len(tabela)):
            linha = tabela.iloc[n_linha]
            self.inserirQSA(linha)