import requests
import validators as vd

# Establish connection with the server
def connect(name, url):

    if not vd.url(url):
        print("invalid url")
        return False

    x = requests.post(url, json={'name':name, 'msg':"I want to connect Darling"})
    if x.status_code == 200:
        return True
    else:
        return False

# Is used to send messages to server
def chat(name, url):
    while True:
        msg = input(">>> Type your message Darling: ")
        myobj = {'msg':msg}

        x = requests.post(url, json=myobj)

        print(x.text)

if __name__=="__main__":
    chat()