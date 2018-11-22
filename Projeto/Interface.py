import tkinter

class TelaInial():
    def __init__(self):
        #Tela inicial
        master = tkinter.Tk()
        master.title('Projeto Stone')
        master.geometry('300x300')

        #Linha 1
        textoCpf = tkinter.Label(text='CNPJ')
        textoCpf.grid(row=0,column=0)
        EntradaCpf = tkinter.Entry()
        EntradaCpf.grid(row=0, column=1)
        #Linha 2
        checkPadrão = tkinter.Checkbutton()
        checkPadrão.grid(row=1,column=0)
        textoCpf2 = tkinter.Label(text='Usar dados padrões')
        textoCpf2.grid(row=1, column=1)
        # Linha 3
        textoCpf = tkinter.Label(text='*separe os dados por virgula')
        textoCpf.grid(row=2, column=0, columnspan=2)

        #Linha 4
        butaoBuscar = tkinter.Button(text='Buscar Dados')
        butaoBuscar.grid(row=3,column=0)
        botaoGuardar = tkinter.Button(text='Salvar Excel')
        botaoGuardar.grid(row=3, column=1)

        #Linha 5: Log

        #Linha 6: Tabela


        master.mainloop()

TelaInial()