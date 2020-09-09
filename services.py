import json
import uuid
from abc import abstractmethod, ABC
from models import User

class DbService(ABC):
    @abstractmethod
    def get_list(): pass

    @abstractmethod
    def retrieve(self, user_id): pass

    @abstractmethod
    def create(self, data): pass

    @abstractmethod
    def update(self, user_id, data): pass

    @abstractmethod
    def delete(self, user_id): pass

class FileDbService(DbService):
    def __init__(self, resource_name: str, filename: str = 'mydb'):
        self.filename = filename

    def get_list(self):
        with open(self.filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            return tables[self.resource_name]

    def retrieve(self, user_id):
        with open(self.filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            return tables[self.resource_name][user_id]

    def create(self, data):
        with open(self.filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            nwid = str(uuid.uuid4())
            data['id'] = newid
            tables_changed['users'][newid] = data
        with open(self.filename, 'w') as mydb:
            mydb.write(tables_changed)

    def update(self, user_id, data):
        with open(self.filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            tables_changed['users'][newid] = data
        with open(self.filename, 'w') as mydb:
            mydb.write(tables_changed)

    def delete(self, user_id):
        with open(self.filename, 'r') as mydb:
            tables = json.loads(mydb.read())
            tables_changed = tables.copy()
            del tables_changed['users']
        with open(self.filename, 'w') as mydb:
            mydb.write(tables_changed)


class UserService:

  RESOURCE_NAME = 'users'

    def __init__(self, db:DbService):
        self.db = db(self.RESOURCE_NAME)

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