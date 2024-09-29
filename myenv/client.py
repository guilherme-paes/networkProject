import socket 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))  

client_socket.sendall(input('Say something to the server: ').encode())

data = client_socket.recv(1024).decode()
print(f"Received data: {data}")

# Close the socket
client_socket.close()
