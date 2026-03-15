
import socket
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0" , 9999))
server.listen(10) #it can have  maximum of 10 clients 11th client will be rejected 
print("The server is listening on port number 9999" )

def handle_single_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024)
        if message.decode() == "Q":
            break
        else:
            print(f"Message from Client: {message.decode()}")
        message = input("Server: ")
        client_socket.send(message.encode())
    client_socket.close()

while True:
    result = server.accept()
    client_socket = result[0]
    client_address = result[1]
    print(f"New connection from {client_address}")
    thread = threading.Thread(target=handle_single_client, args=(client_socket, client_address))
    thread.start()

