#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and adds words. """    
    while True:
        ports = socket.getaddrinfo(socket.gethostname(), 0, socket.AF_INET, socket.SOCK_STREAM)
        for res in ports:
            af, socktype, proto, canonname, sa = res
            