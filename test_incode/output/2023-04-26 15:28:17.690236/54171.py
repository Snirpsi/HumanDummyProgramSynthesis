#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or prints all ports. """    
    
    ports = []
    
    # Open a socket and listen for incoming connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    
    # Accept connections and print their ports
    while True:
        conn, addr = sock.accept()
        ports.append(addr[1])
        
        # Send the response to the client
        conn.send('\n'.join(str(p) for p in ports))
        
        # Close the connection
        conn.close()
        
        # Wait for a new connection
        conn, addr = sock.accept()
        
    # Close the socket and exit
    sock.close()
    
