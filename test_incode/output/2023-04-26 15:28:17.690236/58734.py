#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and returns a port. """    
    
    while True:
        
        ports = socket.getaddrinfo('localhost', 0, socket.AF_INET, socket.SOCK_STREAM)
        
        for res in ports:
            af, socktype, proto, canonname, sa = res
            
            if af == socket.AF_INET:
                