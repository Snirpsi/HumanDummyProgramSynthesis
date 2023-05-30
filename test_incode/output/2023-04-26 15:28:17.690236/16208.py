#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    ports = []
    
    # Open a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 0))
    sock.listen(10)
    
    # Accept the connection and store its port number
    while True:
        conn, addr = sock.accept()
        ports.append(conn.getsockname()[1])
        
        # Close the connection
        conn.close()
        
        # Wait for another connection
        time.sleep(1)
        
    # Close the socket
    sock.close()
    
    # Return the list of ports
    return ports
