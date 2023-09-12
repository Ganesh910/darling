import server
import client
import threading
import time
import subprocess
# import requests

# def ping_url(url):
#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             # URL is reachable
#             return True
        
#     except requests.exceptions.RequestException as e:
#         return False

def start_ngrok(cmd):
    try:
        subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)
    except:
        subprocess.Popen(['x-terminal-emulator', '-e', cmd])

def start_server():
    server.app.run(debug=False)

def start_client():
    name = input("=> Enter Your Name Darling:\n")
    url = input("=> Enter the secret URL Darling:\n")
    if client.connect(name, url):
        client.chat(name, url)

    else :
        print("Nopes! You are not my Darling, Can't talk.")

start_ngrok('ngrok http 5000')
thread_server = threading.Thread(target=start_server)
thread_client = threading.Thread(target=start_client)

thread_server.start()
time.sleep(2)
thread_client.start()
