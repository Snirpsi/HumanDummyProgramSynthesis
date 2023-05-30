#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and returns all ports. """    
    
    ports = []
    
    # iterate over all ports
    for port in range(0, 65535):
        
        # create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # bind the socket to the port
        sock.bind(('localhost', port))
        
        # listen for connections
        sock.listen(1)
        
        # add the port to the list
        ports.append(port)
        
        # close the socket
        sock.close()
    
    # return the list of ports
    return ports
