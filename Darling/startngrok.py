import subprocess
import time
import pyperclip

def run_ngrok(port, authtoken=None):
    # Start Ngrok to expose the local port
    ngrok_command = ['ngrok', 'http', str(port)]
    if authtoken:
        ngrok_command.extend(['-authtoken', authtoken])

    ngrok_process = subprocess.Popen(ngrok_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for Ngrok to generate the forwarding URL
    time.sleep(5)  # Adjust this time based on your needs

    # Get the forwarding URL from Ngrok's output
    ngrok_output = ngrok_process.stdout.read().decode('utf-8')
    lines = ngrok_output.split('\n')
    forwarding_url = None
    for line in lines:
        if line.startswith('Forwarding'):
            forwarding_url = line.split(' ')[1]

    return forwarding_url

if __name__ == '__main__':
    # Replace with your desired port number and, if needed, your Ngrok authtoken
    port = 5000
    authtoken = None  # Replace with your Ngrok authtoken if you have one

    forwarding_url = run_ngrok(port, authtoken)

    if forwarding_url:
        print(f"Forwarding URL: {forwarding_url}")
        pyperclip.copy(forwarding_url)  # Copy the URL to the clipboard
        print("Forwarding URL copied to clipboard.")
    else:
        print("Failed to get the forwarding URL.")
