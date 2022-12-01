from peewee import *

db = SqliteDatabase('projetoterrenos.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(25, unique=True, null=False)
    password = CharField(25, null=False)


class History(BaseModel):
    user = ForeignKeyField(User, to_field='username')
    xExtra = FloatField()
    yExtra = FloatField()
    areaLot = FloatField()
    areaTerrain = FloatField()
    yTerrain = FloatField()
    xTerrain = FloatField()
    cost = FloatField()


class Query:
    @staticmethod
    def create_db():
        User.create_table()
        History.create_table()

    def register_user(self, name, ps):
        try:
            User.insert(username=f'{name}', password=f'{ps}').execute()
            print("Sucesso")
        except NameError:
            print('Erro no Insert', NameError)

    @staticmethod
    def check_exists(name):
        query = User.select()
        for user in query:
            if user.username == name:
                return True
        return False

    @staticmethod
    def auth_user(name, ps):
        found = False
        try:
            query = User.select()
            for user in query:
                if user.username == name:
                    print('Usuário encontrado')
                    if user.password == ps:
                        print('Entrou')
                        return True
                    else:
                        print('Senha incorreta')
                        return False
            if not found:
                print('Usuário não encontrado')
                return False
        except NameError:
            print(NameError)

    @staticmethod
    def log_generator(
            user,
            x_extra,
            y_extra,
            area_lot,
            area_terrain,
            y_terrain,
            x_terrain,
            cost):
        try:
            History.insert(user=f'{user}',
                           xExtra=x_extra,
                           yExtra=y_extra,
                           areaLot=area_lot,
                           areaTerrain=area_terrain,
                           yTerrain=y_terrain,
                           xTerrain=x_terrain,
                           cost=cost
                           ).execute()
            print("Sucesso")
        except NameError:
            print('Erro no log', NameError)

    @staticmethod
    def get_log(user):
        try:
            query = History.select().where(History.user == user).execute()
            lista = []
            for i in query:
                list = [i.user_id,
                        i.xExtra,
                        i.yExtra,
                        i.areaLot,
                        i.areaTerrain,
                        i.yTerrain,
                        i.xTerrain]
                lista.append(list)
            return lista
        except NameError:
            print(NameError)
            print("Sem histórico")
