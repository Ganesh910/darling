import server
import client
import threading
import time

def start_server():
    server.app.run(debug=False)

def start_client():
    name = input(">>> Enter Your Name Darling: ")
    url = input(">>> Enter the secret URL Darling :")
    if client.connect(name, url):
        client.chat(name, url)

    else :
        print("Nopes! You are not my Darling, Can't talk.")

thread_server = threading.Thread(target=start_server)
thread_client = threading.Thread(target=start_client)

thread_server.start()
time.sleep(2)
thread_client.start()
