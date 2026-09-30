import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port number
host = "127.0.0.1"
port = 5000

# Bind socket to IP address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server started...")
print("Waiting for client connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)

# Receive message from client
message = client_socket.recv(1024).decode()

print("Message received from client:", message)

# Send response to client
response = "Hello Client, message received successfully."
client_socket.send(response.encode())

# Close client connection
client_socket.close()

# Close server socket
server_socket.close()

print("Connection closed.")
