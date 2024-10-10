import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 50000))  
server_socket.listen(1)

print("Server is waiting for messages...")


while True:

    connection, address = server_socket.accept()
    print(f"Connected to {address}")

    data = connection.recv(1024).decode()

    print(f"Received data: {data}")
    rdata= data


    connection.sendall(f"Your message '{rdata}' was received successfully!".encode())

    if data.lower() == 'exit':
        break
    else:
        print('Waiting for another messages: ')
    
    
    

    


connection.close()
server_socket.close()
