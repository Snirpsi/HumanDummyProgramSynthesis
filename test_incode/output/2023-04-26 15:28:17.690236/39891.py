#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    port = 8080
    
    # Create a socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    
    # Listen for connections on port 8080
    sock.listen(5)
    
    # Accept connection and print out the request
    while True:
        conn, addr = sock.accept()
        print('Received connection from', addr)
        conn.sendall(b'Hello, world!')
        conn.close()
    
