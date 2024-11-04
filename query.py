from neo4j import GraphDatabase
from database import Database

class Query:
    def __init__(self, db):
        self.db = db

#Questão 1. a)
    def bucsa_prof_nome(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result

# b)
    def busca_prof_m(self):
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.cpf AS cpf
        """
        result = self.db.execute_query(query)
        return result
# c)
    def busca_cidades(self):
        query = """
                MATCH (c:City)
                RETURN c.name AS name
                """
        result = self.db.execute_query(query)
        return result

#d)
    def busca_escola(self):
        query = """
                MATCH (s:School)
                WHERE s.number >= 150 AND s.number <= 550
                RETURN s.name AS name, s.address AS address, s.number AS number
                """
        result = self.db.execute_query(query)
        return result

# Questão 2. a)

    def busca_velho_novo_prof(self):
        query = """
        MATCH (t:Teacher)
        RETURN MIN(t.ano_nasc) AS ano_nasc_mais_velho, MAX(t.ano_nasc) AS ano_nasc_mais_jovem
        """
        result = self.db.execute_query(query)
        return result

# b)
    def busca_media_populacao(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population) AS media_populacao
        """
        result = self.db.execute_query(query)
        return result

# c)
    def busca_cidade_cep(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN replace(c.name, 'a', 'A') AS nome_alterado
        """
        result = self.db.execute_query(query)
        return result

# d)
    def prof_terceira_letra(self):
        query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) AS terceira_letra
        """
        result = self.db.execute_query(query)
        return result
