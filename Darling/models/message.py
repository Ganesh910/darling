class Message:
    def __init__(self, id, sender, receiver, content, time):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.time = time

    def __repr__(self): 
        return f'<{self.sender}: {self.content}>'
    
    def get_id(self):
        return str(self.id)
    
    def get_sender(self):
        return str(self.sender)
    
    def get_receiver(self):
        return str(self.receiver)
    
    def get_content(self):
        return str(self.content)
    
    def get_time(self):
        return str(self.time)

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'receiver': self.receiver,
            'content': self.content,
            'time': self.time
        }
    