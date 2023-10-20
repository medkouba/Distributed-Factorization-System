import socket
import time
import random
import struct
import string
def generate_long_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
# Define the server address and port
server_address = ('127.0.0.1', 12345)

# Create a socket and bind it to the server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)
workers = []

while len(workers) < 2:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    workers.append(connection)
L = [995658762541,995658762541]
# Send each chunk to a worker
for i, worker in enumerate(workers):
    
    # Send the size of the chunk as a 4-byte integer
    worker.send(str(L[i]).encode())
    print(f"Sent chunk to Worker {i + 1}")

# Wait for workers to finish and receive their results
results = ''
start_time=time.time()
for i, worker in enumerate(workers):
    # Receive the result from the worker
    received_data = worker.recv(999999).decode()
    
    results=results+','+received_data
    print(f"Received result {received_data} from Worker {i + 1}")

# Calculate the sum of results
print(results)

# Measure the end time
end_time = time.time()

# Calculate the total time for the server
server_time = end_time - start_time
print(f"Time required for the server: {server_time} seconds")

# Close the connection and the server socket
for worker in workers:
    worker.close()
server_socket.close()