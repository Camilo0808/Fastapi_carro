from database.connection.db_connection import DBConnection

class Carro(DBConnection):
    def new(self, carro):
        try:
            criar_carro = self._connection['Carro'].insert_one(carro)
            return True
        except Exception as e:
            print("Ocorreu o seguinte erro: ", e)
            return False

    def delete_one(self, query):
        try:
            remover_carro = self._connection['Carro'].delete_one(query)
            return True
        except Exception as e:
            print("Ocorreu o seguinte erro: ", e)
            return False

    def update_one(self, query, data):
        try:
            altera_carro = self._connection['Carro'].update_one(query, data)
            return True
        except Exception as e:
            print("Ocorreu o seguinte erro: ", e)
            return False

    def find(self, args, reject={"_id":0}): 
        try:
            selecionar_carro = list(self._connection['Carro'].find(args, reject))
            return selecionar_carro
        except Exception as e:
            print("Ocorreu o seguinte erro: ", e)
            return False