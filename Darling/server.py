from flask import Flask, request, jsonify
import time
from models import Message, User
from typing import Dict
import uuid

app = Flask("Darling")

users: Dict[str, User] = {}


@app.route("/verify/", methods=['POST'])
def verify():
    if request.method == 'POST':
        user_id = 'user' + str(uuid.uuid4()).replace('-', '')
        name = request.get_json()['name']
        user = User(id=user_id, name=name)
        users[user_id] = user
        return user_id

    else:
        print("Not a post request")
        return "Not Success"


@app.route("/", methods=['GET', 'POST'])
def chat_server():

    json_msg = request.get_json()
    user_id = json_msg['user_id']

    if request.method == 'POST':

        # Time of messaged sent by client
        current_time = time.strftime("%H:%M:%S")
        sender_id = user_id
        content = json_msg['msg']
        receiver_id = json_msg['receiver_id']

        message = Message(sender_id=sender_id, time=current_time, content=content, receiver_id=receiver_id)

        # append the message in every inbox
        for user_id in users:
            if user_id != sender_id:
                users[user_id].add_message(message)

        print(f"{json_msg['name']} says : {json_msg['msg']}")

        return "sent"
    
    elif request.method == 'GET':
        new_msgs = []
        q = users[user_id].get_inbox()
        while q:
            msg = q.popleft()
            new_msgs.append(msg.to_dict())
        return jsonify(new_msgs)

    return "Method Not supported Darling :("


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

