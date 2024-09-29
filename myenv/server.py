import socket

# Step 1: Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to an IP and port
server_socket.bind(('localhost', 12345))  # Make sure nothing is named 'bind'

# Step 3: Listen for incoming connections
server_socket.listen(1)

print("Server is waiting for a connection...")

# Step 4: Accept a connection
connection, address = server_socket.accept()
print(f"Connected to {address}")

# Step 5: Receive data from the client
data = connection.recv(1024).decode()
print(f"Received data: {data}")

# Step 6: Send data back to the client
connection.sendall("Hello from server!".encode())

# Close the connection
connection.close()
server_socket.close()
