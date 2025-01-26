import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("[ERROR] Disconnected from server.")
            client_socket.close()
            break

server_ip = input("Enter server IP: ")
server_port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

user = input("Enter your username: ")
client.send(f"{user} has joined the chat!".encode('utf-8'))
print("Type quit to leave the chat")

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    message = input("")
    if message.lower() == "quit":
        client.send(f"{user} has left the chat.".encode('utf-8'))
        client.close()
        break
    client.send(f"{user}: {message}".encode('utf-8'))


print("exiting")
sys.exit()

