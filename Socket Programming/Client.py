import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port number
host = "127.0.0.1"
port = 5000

# Connect to server
client_socket.connect((host, port))

print("Connected to server.")

# Get message from user
message = input("Enter message to send to server: ")

# Send message to server
client_socket.send(message.encode())

# Receive response from server
response = client_socket.recv(1024).decode()

print("Response from server:", response)

# Close connection
client_socket.close()

print("Connection closed.")
