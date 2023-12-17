from collections import deque
from models import Message

class User:
    def __init__(self, id, name, email=None, password=None):
        self.id = id
        self.name = name
        self.inbox = deque()

    def __repr__(self):
        return f'<User: {self.name}>'
    
    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return str(self.name)
    
    def add_message(self, msg: Message):
        self.inbox.append(msg)
    
    def get_inbox(self):
        return self.inbox