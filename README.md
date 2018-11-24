
# Stone
Este é um código feito para cumprir o desafio enviado pela stone.
O programa faz acesso a sua API, pegando seus dados e salvando em um banco de dados de teste.

Após salvo o programa permite acessar os dados e salva-los em um arquivo xlsx.

Existem duas versões do programa. Uma criada em jupyter notebook estando no arquivo, Notebook.ipynb, no qual os comandos estão comentados, e é possível observar as analises durante o codigo. A outra versão esta dividas em diversos arquivos na pasta Projeto, ele esta comentado abaixo. 

O programa também foi compilado e transformado em um arquivo exe, encontrado no caminho:
\Projeto\build\Principal\Principal.exe

Também segue um arquivo chamando dashboard que apresenta uma dashboard Excel com os dados recuperados.

# Funcionamento
Para executar o programa e necessário executar o arquivo Principal.py

É necessário que o estejam instaladas as bibliotecas:
- Pandas 
- requests 
- mysql.connector
- matplotlib 
- pandastable

Podendo ser instalda com o comando:
pip install pandas requests matplotlib pandastable mysql-connector 

Apos executado ira abrir uma interface grafica para acessar os dados. Pode se passar os CNPJs escolhidos, separados por virgula, ou clicar no checkbox para passar os CNPJs de teste.

Ao clicar no botão "Buscar Dados" o programa ira acessar a API e extrair os dados. Quando estiver finalizado a busca ira abrir uma nova aba com o dashboard e as tabelas recuperadas.

Ao se clicar o botão "salvar no DB" será salvo todos os dado no banco de dados.

O banco de dados esta alocado no site  https://www.db4free.net/, podendo ser acessado atraves do phpMyAdmin pelo menos site.


# Estrutura
O programa está divido em tres classes, um responsável pela Extração dos dados da API outra por salva-los no banco de dados e a ultima para inteface.