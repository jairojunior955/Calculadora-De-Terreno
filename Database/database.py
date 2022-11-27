from peewee import *

db = SqliteDatabase('projetoterrenos.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(25, unique=True, null=False)
    password = CharField(25, null=False)


class Query:
    def create_db(self):
        try:
            User.create_table()
        except:
            print('Erro ao criar db')

    def insert_user(self, name, ps):
        try:
            name = input("nome ")
            ps = input("password ")
            user = User.insert(username=f'{name}', password=f'{ps}').execute()
            print("Sucesso")
        except NameError:
            print('Erro no Insert', NameError)

    def auth_user(self, name, ps):
        found = False
        try:
            query = User.select()
            for user in query:
                if user.username == name:
                    print('Usuário encontrado')
                    found = True
                    if user.password == ps:
                        print('Entrou')
                        return True
                        break
                    else:
                        print('Senha incorreta')
                        return False
                        break
            if not found:
                print('Usuário não encontrado')
                return False
        except NameError:
            print(NameError)
