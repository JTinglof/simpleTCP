import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 256 

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (TCP_IP, TCP_PORT)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
waiting = True
while waiting:
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address, file=sys.stderr)
        # Receive the data 
        while True:
            data = connection.recv(BUFFER_SIZE)
            print('received "%s"' % data, file=sys.stderr)
            data = data.decode('utf-8')
            # Converting the data
            newData = ""
            for c in data:
                newData = newData + chr(ord(c) + 1) 
            # Sending the data back
            if data:
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(newData.encode('utf-8'))
            else:
                print('no more data from', client_address, file=sys.stderr)
                waiting = False
                break      
    finally:
        # Clean up the connection
        connection.close()