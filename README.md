
# Stone
Este � um c�digo feito para cumprir o desafio enviado pela stone.
O programa faz acesso a sua API, pegando seus dados e salvando em um banco de dados de teste.

Ap�s salvo o programa permite acessar os dados e salva-los em um arquivo xlsx.

Existem duas vers�es do programa. Uma criada em jupyter notebook estando no arquivo, Notebook.ipynb, no qual os comandos est�o comentados, e � poss�vel observar as analises durante o codigo. A outra vers�o esta dividas em diversos arquivos na pasta Projeto, ele esta comentado abaixo. 

O programa tamb�m foi compilado e transformado em um arquivo exe, encontrado no caminho:
\Projeto\build\Principal\Principal.exe

Tamb�m segue um arquivo chamando dashboard que apresenta uma dashboard Excel com os dados recuperados.

# Funcionamento
Para executar o programa e necess�rio executar o arquivo Principal.py

� necess�rio que o estejam instaladas as bibliotecas:
- Pandas 
- requests 
- mysql.connector
- matplotlib 
- pandastable

Podendo ser instalda com o comando:
pip install pandas requests matplotlib pandastable mysql-connector 

Apos executado ira abrir uma interface grafica para acessar os dados. Pode se passar os CNPJs escolhidos, separados por virgula, ou clicar no checkbox para passar os CNPJs de teste.

Ao clicar no bot�o "Buscar Dados" o programa ira acessar a API e extrair os dados. Quando estiver finalizado a busca ira abrir uma nova aba com o dashboard e as tabelas recuperadas.

Ao se clicar o bot�o "salvar no DB" ser� salvo todos os dado no banco de dados.

O banco de dados esta alocado no site  https://www.db4free.net/, podendo ser acessado atraves do phpMyAdmin pelo menos site.


# Estrutura
O programa est� divido em tres classes, um respons�vel pela Extra��o dos dados da API outra por salva-los no banco de dados e a ultima para inteface.