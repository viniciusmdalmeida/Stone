
# Stone
Este é um código feito para cumprir o desafio enviado pela stone.
O programa faz acesso a uma API, pegando seus dados e salvando em um banco de dados de teste.

Após salvo o programa permite acessar os dados e salva-los em um arquivo xlsx

Existem duas versões do programa. Uma criada em jupyter notebook estando no arquivo, Notebook.ipynb, no qual os comandos estão comentados, e é possível observar as analises durante o codigo. A outra versão esta dividas em diversos arquivos na pasta Projeto, ele esta comentado abaixo. 

Também segue um arquivo chamando dashboard que apresenta uma dashboard Excel com os dados recuperados.

# Funcionamento
Para executar o programa e necessário executar o arquivo Principal.py
E necessário que o estejam instaladas as bibliotecas:
- Pandas 
- requests 
- MySQLdb


Apos executado o programa irá fazer acesso a API, recuperar os dados pedidos, salva-los em um banco de dados SQL e recupera-los do mesmo banco de dados salvando em arquivo xlsx chamando saída.

# Estrutura
O programa está divido em duas classes, um responsável pela Extração dos dados da API outra por salva-los no banco de dados.