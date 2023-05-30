#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports. """    
    while True:
        ports = socket.getaddrinfo('localhost', 0, socket.AF_INET, socket.SOCK_STREAM)
        for family, socktype, proto, canonname, sockaddr in ports:
            