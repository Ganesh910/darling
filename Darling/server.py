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
    if request.method=='POST':

        # Time of messaged sent by client
        current_time = time.strftime("%H:%M:%S")
        json_msg = request.get_json()

        # add time to the json data
        json_msg['time'] = current_time

        # append the json to the keep the history
        convo.append(json_msg)
        
        print(f"{json_msg['name']} says : {json_msg['msg']}")

        return "sent"
    
    elif request.method=='GET':
        ...

# # This route is used to send messages by the client
# @app.route("/", methods=['GET', 'POST'])
# def chat():
#     if request.method == 'POST':
#         json_msg = request.get_json()
#         print(f"{json_msg['name']} : {json_msg['msg']}")
#         return "Sent"

#     else:
#         return "Not recieved"

# # This route is used when someone wants to connect to you
# @app.route("/connect", methods=['GET', 'POST'])
# def connect():
#     if request.method == 'POST':
#         json_msg = request.get_json()
#         print(f"You can now recieve messages from {json_msg['name']}")
#         return "I'm listening Darling"

#     else :
#         return "No Darling, We can't talk!"
    
if __name__=="__main__":
    app.run(debug=True)

    # localhost:4040/status
    # http://localhost:4040/api/tunnels