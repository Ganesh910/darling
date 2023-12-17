import curses
import threading
import time
import sys
import requests
import json
import validators

class TerminalUI:
    def __init__(self, stdscr, data):
        self.stdscr = stdscr
        self.chat_history = []
        self.input_message = ""
        self.message_fetcher_thread = threading.Thread(target=self.fetch_messages)
        self.message_fetcher_thread.daemon = True  # Set the thread as daemon so it exits when the main program exits
        self.data = data

    def fetch_messages(self):
        while True:
            time.sleep(1)
            response = requests.get(
                self.data['url']+'/', json={'user_id': self.data['user_id']})
            
            if response.status_code == 200:
                new_msgs = json.loads(response.text)
                self.chat_history.extend(new_msgs)
                continue

            print("Error in fetching messages")

    def display_chat_history(self):
        # Display the chat history in the first part of the screen
        self.stdscr.addstr(0, 0, "Chat History:")
        for i, message in enumerate(self.chat_history):
            self.stdscr.addstr(i + 1, 0, f'{message["time"]} > {message["sender_id"]} says : {message["content"]}')

    def get_input(self):
        # Get input from the user
        curses.echo()  # Enable echoing of characters
        self.stdscr.addstr(curses.LINES - 1, 0, "Type a message: ")
        self.input_message = self.stdscr.getstr(curses.LINES - 1, len("Type a message: "))

        if self.input_message.strip() == b"":
            return
        
        # Check if the user entered "!quit" and exit if true
        if self.input_message.strip() == b"!quit":
            curses.endwin()
            sys.exit()
        
        msg_to_add = {}
        msg_to_add['time'] = time.strftime("%H:%M:%S")
        msg_to_add['sender_id'] = self.data['user_id']
        msg_to_add['content'] = self.input_message.decode("utf-8")
        self.chat_history.append(msg_to_add)

        myobj = {'name': self.data['user_id'], 'msg': self.input_message.decode("utf-8"),
                 'user_id': self.data['user_id'], 'receiver_id': 'all'}

        requests.post(self.data['url']+'/', json=myobj)

        curses.noecho()  # Disable echoing

    def run(self):
        self.message_fetcher_thread.start()  # Start the message fetching thread

        while True:
            self.stdscr.clear()
            self.display_chat_history()
            self.get_input()
    
def prompt():
    name = input("Enter you name Darling :\n")
    url = ""

    role = input(
        "Mode:\n\tType 'server' to create your own server\n\tType 'url' to enter the url\n\tType 'exit' to exit the terminal\n")
    if role == 'server':
        url = 'http://127.0.0.1:6969/'
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

def main():
    data = prompt()
    user_id = verify(data['name'], data['url'])
    data['user_id'] = user_id

    ui = TerminalUI(curses.initscr(), data)
    ui.run()

if __name__ == "__main__":
    main()
