#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        ports = socket.getaddrinfo('localhost', 0, socket.AF_INET, socket.SOCK_STREAM)
        for family, socktype, proto, canonname, sockaddr in ports:
            sock = socket.socket(family, socktype, proto)
            sock.bind(sockaddr)
            sock.listen(1)
            print('Listening on port %s' % sock.getsockname()[1])
            
