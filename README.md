
# Stone
Este � um c�digo feito para cumprir o desafio enviado pela stone.
O programa faz acesso a uma API, pegando seus dados e salvando em um banco de dados de teste.

Ap�s salvo o programa permite acessar os dados e salva-los em um arquivo xlsx

Existem duas vers�es do programa. Uma criada em jupyter notebook estando no arquivo, Notebook.ipynb, no qual os comandos est�o comentados, e � poss�vel observar as analises durante o codigo. A outra vers�o esta dividas em diversos arquivos na pasta Projeto, ele esta comentado abaixo. 

Tamb�m segue um arquivo chamando dashboard que apresenta uma dashboard Excel com os dados recuperados.

# Funcionamento
Para executar o programa e necess�rio executar o arquivo Principal.py
E necess�rio que o estejam instaladas as bibliotecas:
- Pandas 
- requests 
- MySQLdb


Apos executado o programa ir� fazer acesso a API, recuperar os dados pedidos, salva-los em um banco de dados SQL e recupera-los do mesmo banco de dados salvando em arquivo xlsx chamando sa�da.

# Estrutura
O programa est� divido em duas classes, um respons�vel pela Extra��o dos dados da API outra por salva-los no banco de dados.