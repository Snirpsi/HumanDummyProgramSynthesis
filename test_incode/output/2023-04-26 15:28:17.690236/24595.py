#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and stores a port. """    
    port = int(sys.argv[1])
    
    # Create a socket and bind it to the port we want
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    
    # Listen for connections
    sock.listen(10)
    
    # Wait for connections
    while True:
        # Accept a connection
        conn, addr = sock.accept()
        
        # Send a response
        conn.send('Hello World!')
        
        # Close the connection
        conn.close()
        
        # 