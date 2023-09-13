from flask import Flask, request
import time
from collections import deque

app = Flask("Darling")

convo = []


@app.route("/verify", methods=['POST'])
def verify():
    ...


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

        print(f"{json_msg['name']} says : {json_msg['msg']}")

        return "sent"

    elif request.method == 'GET':
        ...


if __name__ == "__main__":
    app.run(debug=True)
