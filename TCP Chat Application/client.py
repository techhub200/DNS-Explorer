import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999)) #Client sends SYN
print("Connected to Server")
while True:
 message=input("CLIENT MESSAGE-> ")
 if message=="Q":
  client.send(message.encode())
  break
 else:
  client.send(message.encode())
  returned_message = client.recv(1024)
  print(f"SERVER-> {returned_message.decode()}")