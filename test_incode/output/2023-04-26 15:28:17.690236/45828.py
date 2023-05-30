#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    # Open the port and start listening for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept connections.
    while True:
        connection, address = sock.accept()
        print('Connected by', address)
        
        # Receive the whole message in one chunk.
        message = connection.recv(1024)
        
        # Send the message back to the client.
        connection.send(message)
        
        # Close the connection.
        connection.close()
        
        # 