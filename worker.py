import socket
import time
import struct
import string

# Define the server address and port
server_address = ('127.0.0.1', 12345)
def factorize(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number = number // i
        if number == 1:
            break
    return factors
# Create a socket and connect to the server
worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
worker_socket.connect(server_address)
results = worker_socket.recv(9999999999).decode()

print(f"Received chunk from the server:")
print(int(results))
p=factorize(int(results))
result=''
for i in p:
    result=result+str(i)


# Send the count back to the server
worker_socket.send(str(result).encode())
print(f"Sent count {result} to the server")
# Close the connection
worker_socket.close()