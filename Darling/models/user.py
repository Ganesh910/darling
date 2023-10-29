class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<User: {self.name}>'
    
    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return str(self.name)
    