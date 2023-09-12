from flask import Flask, request

app = Flask("Darling")

# This route is used to send messages by the client
@app.route("/", methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        json_msg = request.get_json()
        print(f"{json_msg['name']} : {json_msg['msg']}")
        return "Sent"

    else:
        return "Not recieved"

# This route is used when someone wants to connect to you
@app.route("/connect", methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        json_msg = request.get_json()
        print(f"You can now recieve messages from {json_msg['name']}")
        return "I'm listening Darling"

    else :
        return "No Darling, We can't talk!"
    
if __name__=="__main__":
    app.run(debug=True)

    # localhost:4040/status
    # http://localhost:4040/api/tunnels