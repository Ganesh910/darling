import requests
import validators
import threading
import time
import json

# Prompt for the mode of chatting
def prompt():
    name = input("Enter you name Darling :\n")
    url = ""

    role = input(
        "Mode:\n\tType 'server' to create your own server\n\tType 'url' to enter the url\n\tType 'exit' to exit the terminal\n")
    if role == 'server':
        url = 'http://127.0.0.1:5000/'
        print("Server Successfully created!")

    elif role == 'url':

        # ask for the url until it's valid
        while True:
            url = input("Invalid URL! Retry Beauty!\n")

            if validators.url(url):
                break
            else:
                print("Darling! It's not valid url. Please Try Again.")

    elif role == 'exit':
        print("Bye Darling! See you soon!")
        exit()

    else:
        print("Please enter one of the command only. (case sensitive)")

    return {'name': name, 'url': url}


# Verifies the users. Authentication
def verify(name, url):
    # Create profile
    myobj = {'name': name}
    response = requests.post(url+'/verify/', json=myobj)

    if response.status_code == 200:
        user_id = response.text
        print("Darling, Your profile is ready")
    else:
        print("Sorry Darling! Unable to create your Profile")
        exit()
    return user_id


# Send messages
def send(name, url, user_id):
    while True:
        msg = input("=> Darling, ")
        myobj = {'name': name, 'msg': msg,
                 'user_id': user_id, 'receiver_id': 'all'}

        response = requests.post(url+'/', json=myobj)
        if response.status_code == 200:
            print("Sent")


# Receive Messages
def get(url, user_id):
    while True:
        time.sleep(1)
        response = requests.get(
            url+'/', json={'user_id': user_id})
        new_msgs = json.loads(response.text)

        for new_msg in new_msgs:
            print(
                f"{new_msg['time']} > {new_msg['name']} says : {new_msg['msg']}")


if __name__ == '__main__':
    data = prompt()
    user_id = verify(**data)
    data['user_id'] = user_id
    getThread = threading.Thread(target=get, args=[data['url'], user_id])
    sendThread = threading.Thread(target=send, args=[*data.values()])

    getThread.start()
    sendThread.start()

    getThread.join()
    sendThread.join()
