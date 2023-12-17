from models import Message
from typing import List

class Chat:

    def __init__(self) -> None:
        self.chat = []

    def add(self, message: Message):
        self.chat.append(message)

    def get_chat(self) -> List[Message]:
        return self.chat