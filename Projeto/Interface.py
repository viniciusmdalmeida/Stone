from tkinter import *
import tkinter.ttk  as ttk
import threading
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.ttk import Notebook
from pandastable import Table, TableModel

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

from BancoDados import BancoDados
from ExtraçãoDados import *


class TelaInial():
    linkBase = 'https://www.receitaws.com.br/v1/cnpj/'
    cnpjs = [16501555000157, 14994237000140, 18727053000174]#, 13966572000171, 12839955000116, 16569357000125,16575851000100, 12592831000189]

    def __init__(self):
        #Tela inicial
        self.master = Tk()
        self.master.title('Projeto Stone')
        framePrincipal = Frame(self.master, borderwidth=1, relief="solid",padx=10,pady=5)
        framePrincipal.pack(fill=Y,side=LEFT)

        #Linha 1
        textoCpf = Label(framePrincipal,text='CNPJ')
        textoCpf.grid(row=0,column=0,sticky=W)
        self.EntradaCpf = Entry(framePrincipal, width=35)
        self.EntradaCpf.grid(row=0, column=1,sticky=W,columnspan=2)
        #Linha 2
        self.check = IntVar()
        checkPadrão = Checkbutton(framePrincipal,text="Usar dados padrões",command=self.checkButton,variable=self.check)
        checkPadrão.grid(row=1,column=1,sticky=W)
        # Linha 3
        textoCpf = Label(framePrincipal,text='obs: separe os dados por virgula')
        textoCpf.grid(row=2, column=1, columnspan=2,sticky=W)
        #Linha 4
        self.butaoBuscar = Button(framePrincipal,text='Buscar Dados',command=self.criarTabela)
        self.butaoBuscar.grid(row=3,column=0,sticky=W)
        self.botaoGuardar = Button(framePrincipal,text='Salvar no BD',command=self.salvarBD,state = DISABLED)
        self.botaoGuardar.grid(row=3, column=2,sticky=E)
        #Log
        frameLog = Frame(framePrincipal)
        frameLog.grid(row=4,column=0,columnspan=3)
        self.labelLog = Label(frameLog,text="Log:",pady=2)
        self.labelLog.pack()
        self.textLog = Text(frameLog,height=22, width=35)
        self.textLog.pack()

        self.master.mainloop()

    def checkButton(self):
        if self.check.get():
            self.cnpjs = [16501555000157, 14994237000140,18727053000174, 13966572000171, 12839955000116, 16569357000125,16575851000100, 12592831000189]
            print(self.cnpjs)
            self.EntradaCpf['state'] = DISABLED

        else:
            self.EntradaCpf['state'] = NORMAL


    def criarTabelaThread(self):
        if not self.check.get():
            self.cnpjs = self.EntradaCpf.get()
            self.cnpjs = self.cnpjs.split(',')
            for i in range(len(self.cnpjs)):
                self.cnpjs[i] = int(self.cnpjs[i].strip())
            print(self.cnpjs)
        if len(self.cnpjs) == 0:
            self.textLog.insert(END,"Digite CNPJS")
            return

        self.butaoBuscar['state'] = DISABLED
        self.textLog.insert(END, "Iniciando Busca ...\n")
        frame2 = Frame(self.master)
        frame2.pack()

        tabs = Notebook(frame2)

        frameNotebook1 = Frame(tabs)
        frameNotebook2 = Frame(tabs)
        frameNotebook3 = Frame(tabs)

        self.dfComp, self.dfQSA = pegarDadosLista(self.linkBase, self.cnpjs,interface=True,textLabel=self.textLog)
        self.textLog.insert(END,"Busca Finalizada\n")

        tabelaComp = Table(frameNotebook2, dataframe=self.dfComp,showtoolbar=True, showstatusbar=True)
        tabelaComp.show()
        tabelaComp = Table(frameNotebook3, dataframe=self.dfQSA,showtoolbar=True, showstatusbar=True)
        tabelaComp.show()
        self.criarDashboard(frameNotebook1)

        tabs.add(frameNotebook1, text="DashBoard")
        tabs.add(frameNotebook2,text="Companhias")
        tabs.add(frameNotebook3,text="QSA")
        self.butaoBuscar['state'] = NORMAL
        self.botaoGuardar['state'] = NORMAL
        tabs.pack()

    def criarTabela(self):
        t1 = threading.Thread(target=self.criarTabelaThread)
        t1.start()
        # t1.join()

    def salvarBDThread(self):
        self.textLog.insert(END, "Salvando no Banco de Dados")
        bancoDados = BancoDados()

        if not bancoDados.tabelaExiste():
            bancoDados.criarTabelas()

        bancoDados.escreverCompanhias(self.dfComp)
        bancoDados.escreverQSA(self.dfQSA)

    def salvarBD(self):
        t1 = threading.Thread(target=self.salvarBDThread())
        t1.start()

    def criarDashboard(self,tela):
        frame1 = Frame(tela)
        frame1.pack()
        frame2 = Frame(tela)
        frame2.pack()

        self.verificarCapital(frame1)
        self.listarAcionista(frame2)



    def verificarCapital(self,frame):
        frameImage = Frame(frame)
        frameImage.pack(side=LEFT)
        frameBarra = Frame(frame)
        frameBarra.pack(side=LEFT)
        frameTabela = Frame(frame)
        frameTabela.pack(side=LEFT)
        self.TabelaComp = ttk.Treeview(frameTabela)

        self.plotGrafico(frameImage,0)
        w = Scale(frameBarra, to=len(self.dfComp),command=lambda value:self.plotGrafico(frameImage,int(value)))
        w.pack()

        self.TabelaComp["columns"] = ("Nome", "capital")
        self.TabelaComp.pack()

        self.TabelaComp.column("#0", width=50)
        self.TabelaComp.column("Nome", width=200)
        self.TabelaComp.column("capital", width=100)
        self.TabelaComp.heading("#0", text="id")
        self.TabelaComp.heading("Nome", text="Nome")
        self.TabelaComp.heading("capital", text="Valor")




    def listarAcionista(self,frame):
        dfAcionistas = self.dfQSA.groupby('nome').count()
        dfAcionistas.drop('qual', axis=1, inplace=True)
        dfAcionistas['nome'] = dfAcionistas.index
        dfAcionistas = dfAcionistas[dfAcionistas['CNPJ'] > 1]
        dfAcionistas.sort_values(by='CNPJ', ascending=False)
        dfAcionistas.columns = ["Num CNPJs","Nome"]

        tabelaAcionistas = ttk.Treeview(frame)
        tabelaAcionistas["columns"] = ("Nome","Num CNPJ",)
        tabelaAcionistas.pack()
        tabelaAcionistas.column("#0", width=50)
        tabelaAcionistas.column("Nome", width=400)
        tabelaAcionistas.column("Num CNPJ", width=100)
        tabelaAcionistas.heading("#0", text="id")
        tabelaAcionistas.heading("Nome", text="Nome")
        tabelaAcionistas.heading("Num CNPJ", text="Valor")

        cont = 0
        for nome in dfAcionistas.index:
            item = (nome,dfAcionistas.loc[nome]['Num CNPJs'])
            tabelaAcionistas.insert('', 'end', text=cont, value=item)
            cont += 1


    def plotGrafico(self,frame,num=0):
        # self.canvas.get_tk_widget().destroy()
        dados = self.dfComp.set_index('nome')
        if num != 0:
            dados = dados.capital_social.sort_values(ascending=False)[:num]
        else:
            dados = dados.capital_social.sort_values(ascending=False)
        figura = plt.figure(figsize=(2, 2))
        plt.pie(dados, autopct='%1.1f%%')
        plt.legend(labels=self.dfComp['nome'], bbox_to_anchor=(0.5, -0.2))
        self.canvas = FigureCanvasTkAgg(figura , master=frame)
        self.canvas.get_tk_widget().grid(row=1,column=1)

        # self.TabelaComp.delete(self.TabelaComp.get_children())
        for filho in self.TabelaComp.get_children():
            self.TabelaComp.delete(filho)

        cont = 0
        for indice in dados.index:
            item = (indice,dados[indice])
            self.TabelaComp.insert('', 'end', text=cont,value=item)
            cont += 1


