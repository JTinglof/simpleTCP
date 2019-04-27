import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 256

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ((TCP_IP, TCP_PORT))
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

# Prevent the sending of a message that is too large
missingInput = True
while missingInput:
    message = input("Type whatever! ")
    if len(message) > BUFFER_SIZE:
        print("Too long! Try again!")
    else:
        missingInput = False

try:
    
    # Send data
    print('sending "%s"' % message, file=sys.stderr)
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    
    # Receive the new data
    while amount_received < BUFFER_SIZE:
        data = sock.recv(BUFFER_SIZE)
        amount_received += len(data)
        print('received "%s"' % data.decode('utf-8'), file=sys.stderr)

# Clean up the connection
finally:
    print('closing socket', file=sys.stderr)
    sock.close()