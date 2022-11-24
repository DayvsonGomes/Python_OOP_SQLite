#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
dayvson = Pessoa(1, "Dayvson Gomes")
print(dayvson)

#Quero mostrar só o nome
print(dayvson.nome)

#chama o objeto do banco de dados
db = Database()

#instancia o objeto 
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)

#Quero carregar uma lista ue veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

#criar um objeto com qualquer ator/atriz/diretor
novo = pessoa(0, "Batmam")
#Omuito simples
novo = pessoa.save(novo)

#consulta no banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)
  