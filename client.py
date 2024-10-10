import socket 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 50000))  

    
while True:  

    message = input('Send a message to the server (send "exit" to end connection): ')
    
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Server's answer: {data}")

    if message.upper() == 'exit':
        break


client_socket.close()
