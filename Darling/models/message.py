class Message:
    def __init__(self, sender_id, content, time, receiver_id='all'):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.time = time

    def __repr__(self): 
        return f'<{self.sender_id}: {self.content}>'
    
    def get_sender_id(self):
        return str(self.sender_id)
    
    def get_receiver_id(self):
        return str(self.receiver_id)
    
    def get_content(self):
        return str(self.content)
    
    def get_time(self):
        return str(self.time)

    def to_dict(self):
        return {
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'content': self.content,
            'time': self.time
        }
    