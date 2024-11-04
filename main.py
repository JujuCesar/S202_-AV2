from database import Database
from query import Query
from teacherCRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.89.252.203:7687", "neo4j", "rigs-nines-racks")
# db.drop_all()

# Questão 1
# a) Buscando professor com nome Renzo e retornando CPF e Ano de nascimento

query= Query(db)
result = query.bucsa_prof_nome("Renzo")

for record in result:
    print(f"Ano de Nascimento: {record['ano_nasc']}, CPF: {record['cpf']}")

# b) Buscando profs com a letra M e retornando Nome e CPF

result = query.busca_prof_m()

for record in result:
    print(f"Ano de Nascimento: {record['name']}, CPF: {record['cpf']}")

# c) Buscando todas as cidades e retornando-os

result = query.busca_cidades()

for record in result:
    print(f"Nome da Cidade: {record['name']}")

# d) Buscando escolas com number _ 150 e <= 550, retornando nome, endereço e numero

result = query.busca_escola()

for record in result:
    print(f"Nome da Escola: {record['name']}, Endereço: {record['address']}, Número: {record['number']}")


# Questão 2. a)

result = query.busca_velho_novo_prof()

for record in result:
    print(f"Ano de Nascimento do Professor Mais Velho: {record['ano_nasc_mais_velho']}")
    print(f"Ano de Nascimento do Professor Mais Jovem: {record['ano_nasc_mais_jovem']}")

# b)

result = query.busca_media_populacao()

for record in result:
    print(f"Média de habitantes das cidades: {record['media_populacao']}")

# c)

result = query.busca_cidade_cep()

for record in result:
    print(f"Nome da cidade com 'a' substituído por 'A': {record['nome_alterado']}")

# d)

result = query.prof_terceira_letra()

for record in result:
    print(f"Terceira letra do nome do professor: {record['terceira_letra']}")

db.close()


# Questão 3

# Instanciando TeacharCrud

teathcer_crud = TeacherCRUD(db)

# Criando um professor

teathcer_crud.create_teacher("Chris Lima", "189.052.396-66", 1980)

# Buscando um professor
result = teathcer_crud.read_teacher("Chris Lima")
for record in result:
    print(f"Nome: {record['name']}, CPF: {record['cpf']}, Ano de Nascimento: {record['ano_nasc']}")

# Alterando CPF do professor

teathcer_crud.update_teacher("Chris Lima", "162.052.777-77", 1956)


