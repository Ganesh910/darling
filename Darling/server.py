from flask import Flask, request
import time
from collections import deque

app = Flask("Darling")

convo = []

user_id_number = 0

users = {}


@app.route("/verify/", methods=['POST'])
def verify():
    if request.method == 'POST':
        user_id = 'user' + str(user_id_number)
        q = deque()
        users[user_id] = q
        return user_id

    else:
        print("Not a post request")
        return "Not Success"


@app.route("/", methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':

        # Time of messaged sent by client
        current_time = time.strftime("%H:%M:%S")
        json_msg = request.get_json()

        # add time to the json data
        json_msg['time'] = current_time

        # append the json to the keep the history
        convo.append(json_msg)
        users[json_msg['user_id']].append(json_msg)

        print(f"{json_msg['name']} says : {json_msg['msg']}")

        return "sent"

    elif request.method == 'GET':
        ...


if __name__ == "__main__":
    app.run(debug=True)
