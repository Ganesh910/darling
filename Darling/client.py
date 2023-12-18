'''
This is the client side of the chat application.
It uses curses to display the chat history and the input area.
'''

import curses
import threading
import time
import sys
import json
import requests
import validators

class TerminalUI:
    """
    A class to represent a terminal-based chat user interface.
    """

    def __init__(self, stdscr, data):
        self.stdscr = stdscr
        self.chat_history = []
        self.input_message = ""
        self.message_fetcher_thread = threading.Thread(target=self.fetch_messages)
        # Set the thread as daemon so it exits when the main program exits
        self.message_fetcher_thread.daemon = True
        self.data = data
        height, width = stdscr.getmaxyx()

        # Define the chat display area
        chat_display_height = height - 1  # Leave one line for the typing area
        chat_display_width = width
        self.chat_display = stdscr.derwin(chat_display_height, chat_display_width, 0, 0)

    def fetch_messages(self):
        '''
        Fetches messages from the server and updates the chat history.
        '''

        self.display_chat_history()
        while True:
            new_msg_flag = False
            response = requests.get(
                self.data['url']+'/', json={'user_id': self.data['user_id']}, timeout=10)

            if response.status_code == 200:
                new_msgs = json.loads(response.text)
                if len(new_msgs) > 0:
                    new_msg_flag = True
                    self.chat_history.extend(new_msgs)

                if new_msg_flag:
                    self.display_chat_history()
                    new_msg_flag = False

            else:
                print("Error in fetching messages")

            time.sleep(1)

    def display_chat_history(self):
        '''
        Displays the chat history on the screen.
        '''

        # Display the chat history in the first part of the screen
        self.chat_display.clear()
        self.chat_display.addstr(0, 0, "Chat History:")
        for i, message in enumerate(self.chat_history):
            self.chat_display.addstr(
                i + 1, 0, f'{message["time"]} > {message["sender_id"]} says : {message["content"]}')
        self.chat_display.refresh()

    def get_input(self):
        '''
        Gets input from the user and sends it to the server.
        '''

        # Get input from the user
        curses.echo()  # Enable echoing of characters
        self.stdscr.addstr(curses.LINES - 1, 0, "Type a message: ") # pylint: disable=no-member
        self.input_message = self.stdscr.getstr(curses.LINES - 1, len("Type a message: ")) # pylint: disable=no-member
        self.stdscr.clrtoeol()  # Clear to the end of line

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
        self.display_chat_history()

        myobj = {'name': self.data['user_id'], 'msg': self.input_message.decode("utf-8"),
                 'user_id': self.data['user_id'], 'receiver_id': 'all'}

        requests.post(self.data['url']+'/', json=myobj, timeout=10)

        curses.noecho()  # Disable echoing

    def run(self):
        '''
        Runs the chat UI.
        '''

        self.message_fetcher_thread.start()  # Start the message fetching thread

        while True:
            self.get_input()

def prompt():
    '''
    Prompts the user for the name and the url of the server.
    '''

    name = input("Enter you name Darling :\n")
    url = ""

    role = input(
        "Mode:\n\t"
        "Type 'server' to create your own server\n\t"
        "Type 'url' to enter the url\n\t"
        "Type 'exit' to exit the terminal\n"
        )

    if role == 'server':
        url = 'http://localhost:6969/'
        print("Server Successfully created!")

    elif role == 'url':

        # ask for the url until it's valid
        while True:
            url = input("Enter Url: \n=>")

            if validators.url(url):
                break

            print("Darling! It's not valid url. Please Try Again.")

    elif role == 'exit':
        print("Bye Darling! See you soon!")
        sys.exit()

    else:
        print("Please enter one of the command only. (case sensitive)")

    return {'name': name, 'url': url}

# Verifies the users. Authentication
def verify(name, url):
    '''
    Verifies the user by sending a post request to the server.
    '''

    # Create profile
    myobj = {'name': name}
    response = requests.post(url+'/verify/', json=myobj, timeout=10)

    if response.status_code == 200:
        user_id = response.text
        print("Darling, Your profile is ready")
    else:
        print("Sorry Darling! Unable to create your Profile")
        sys.exit()
    return user_id

def main():
    '''
    The main function.
    '''

    data = prompt()
    user_id = verify(data['name'], data['url'])
    data['user_id'] = user_id

    ui = TerminalUI(curses.initscr(), data)
    ui.run()

if __name__ == "__main__":
    main()
