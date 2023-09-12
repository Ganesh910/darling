import requests
import validators

# Establish connection with the server
def connect(name, url):

    if not validators.url(url):
        return False

    x = requests.post(url+'/connect', json={'name':name, 'msg':"I want to connect Darling"})
    if x.status_code == 200:
        print(f"Connection Established with {name} succesfully")
        return True
    else:
        return False

# Is used to send messages to server
def chat(name, url):
    while True:
        msg = input("=> Darling, ")
        myobj = {'name':name, 'msg':msg}

        x = requests.post(url+'/', json=myobj)
        if x.status_code==200:
            print("Sent")

if __name__=="__main__":
    chat()