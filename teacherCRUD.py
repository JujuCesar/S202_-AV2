class TeacherCRUD:
    def __init__(self, database):
        self.db = database

# Método para criar um professor
    def create_teacher(self, name, cpf, ano_nasc):
        query = """
        CREATE (t:Teacher {name: $name, cpf: $cpf, ano_nasc: $ano_nasc})
        """
        parameters = {"name": name, "cpf": cpf, "ano_nasc": ano_nasc}
        self.db.execute_query(query, parameters)

# Método para ler informações de um professor pelo nome
    def read_teacher(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.cpf AS cpf, t.ano_nasc AS ano_nasc
        """
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

# Método para atualizar informações de um professor
    def update_teacher(self, name, new_cpf=None, new_ano_nasc=None):
        # Atualiza apenas os campos que são passados como parâmetros
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = coalesce($new_cpf, t.cpf),
            t.ano_nasc = coalesce($new_ano_nasc, t.ano_nasc)
        RETURN t.name AS name, t.cpf AS cpf, t.ano_nasc AS ano_nasc
        """
        parameters = {"name": name, "new_cpf": new_cpf, "new_ano_nasc": new_ano_nasc}
        return self.db.execute_query(query, parameters)

# Método para deletar um professor
    def delete_teacher(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
