#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or enumerates all ports. """    
    
    while True:
        
        # Open the port and print out its contents.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        sock.listen(1)
        print('Listening on port {}'.format(sock.getsockname()[1]))
        
        # Accept a connection and print out the client address.
        conn, addr = sock.accept()
        print('Connected by', addr)
        
        # Receive the fruits from the client.
        fruit = conn.recv(1024)
        print('Received fruit 