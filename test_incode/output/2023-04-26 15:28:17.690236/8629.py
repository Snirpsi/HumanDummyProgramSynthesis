#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and opens all ports. """    
    
    ports_to_close = []
    
    # Open all ports
    for port in range(0, 65535):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", port))
        server.listen(1)
        ports_to_close.append(port)
        
    # Remove all ports
    for port in ports_to_close:
        server.close