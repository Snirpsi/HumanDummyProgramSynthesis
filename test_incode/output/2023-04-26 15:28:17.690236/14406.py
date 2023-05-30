#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    while True:
        
        # Open the ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        sock.listen(1)
        
        # Accept connections
        conn, addr = sock.accept()
        
        # Do something with the connection
        conn.send('Hello World!')
        
        # Close the connection
        conn.close()
        
        # Wait for the next connection
        