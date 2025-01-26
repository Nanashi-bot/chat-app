import socket
import threading
import time

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected at {time.ctime()}.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            print(f"[DISCONNECTED] {client_address} disconnected.")
            break


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)


server_ip = "0.0.0.0"  # Bind to all interfaces
server_port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((server_ip, server_port))
server.bind(('', server_port))
print("Socket created and bound to port:", server_port)
server.listen(5)

print("[LISTENING] Server is running on ip:",server_ip)
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
