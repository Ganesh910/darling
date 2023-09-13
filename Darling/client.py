import requests
import validators
import threading

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
            url = input("Enter the Url Darlo!")

            if validators.url(url):
                break
            else:
                print("Darling! It's not valid url. Please Try Again.")

    elif role == 'exit':
        print("Bye Darling! See you soon!")
        exit()

    else:
        print("Please enter one the command only. (case sensitive)")

    return (name, url)


# Verifies the users. Authentication
def verify(name, url):

    # Create profile
    myobj = {'name': name}
    response = requests.post(url+'/verify/', json=myobj)

    if response.status_code == 200:
        print("Darling, Your profile is ready")
    else:
        print("Sorry Darling! Unable to create your Profile")
        exit()

# Send messages


def send(name, url):
    while True:
        msg = input("=> Darling, ")
        myobj = {'name': name, 'msg': msg}

        response = requests.post(url+'/', json=myobj)
        if response.status_code == 200:
            print("Sent")


# Receive Messages
def get():
    ...


data = prompt()
# verify(*data)
getThread = threading.Thread(target=get)
sendThread = threading.Thread(target=send, args=[*data])

getThread.start()
sendThread.start()

getThread.join()
sendThread.join()
