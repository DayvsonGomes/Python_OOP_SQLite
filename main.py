#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
dayvson = Pessoa(1, "Dayvson Gomes")
print(dayvson)

#Quero mostrar só o nome
print(dayvson.nome)