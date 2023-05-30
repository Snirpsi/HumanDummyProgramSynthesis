#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = []
    
    # Open a socket to listen on all available ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(5)
    
    # Accept connections from clients
    while True:
        conn, addr = sock.accept()
        
        # Accept connections on all available ports
        for port in range(0, 65535):
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            conn.bind(('', port))
            conn.listen(5)
            
            # Accept connections on all available ports
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
            
            # Accept connections on all available ports
            conn.listen(5)
            
            ports.append(port)
            
        conn.close()
        
        # Print the port number
        print('Server listening on port ' + str(port