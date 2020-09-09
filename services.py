import json
import uuid
from abc import abstrastclass, ABC
from models import User

class DbService(ABC):
    @abstrastclass
    def get_list(): pass

    @abstrastclass
    def retrieve(self, user_id): pass

    @abstrastclass
    def create(self, data): pass

    @abstrastclass
    def update(self, user_id, data): pass

    @abstrastclass
    def delete(self, user_id): pass

class FileDbService(DbService):
    def __init__(self, resource_name: str, filename: str):
        self.filename = filename

    def get_list(self):
        with open(filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            return tables[self.resource_name]

    def retrieve(self, user_id):
        with open(filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            return tables[self.resource_name][user_id]

    def create(self, data):
        with open(filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            nwid = str(uuid.uuid4())
            data['id'] = newid
            tables_changed['users'][newid] = data
        with open(filename, 'w') as mydb:
            mydb.write(tables_changed)

    def update(self, user_id, data):
        with open(filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            tables_changed['users'][newid] = data
        with open(filename, 'w') as mydb:
            mydb.write(tables_changed)

    def delete(self, user_id):
        with open(filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            del tables_changed['users']
        with open(filename, 'w') as mydb:
            mydb.write(tables_changed)


class UserService:

  RESOURCE_NAME = 'users'

    def __init__(self, db:DbService):
        self.db = db(RESOURCE_NAME)

    def get_list(self):
        return self.db.get_list()

    def retrieve(self, user_id: int) -> User:
        return self.as_user(self.db.retrieve(user_id))
    
    def create(self, data: dict) -> User:
        return self.as_user(self.db.create(data))

    def update(self, user_id: int, data: dict) -> User:
        return self.as_user(self.db.update(user_id, data))

    def as_user(self, data: dict) -> User
        return User(**data)

    def delete(self, user_id: int) ->None
        self.db.delete(user_id)