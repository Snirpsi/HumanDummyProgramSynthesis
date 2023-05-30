#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        ports = socket.getaddrinfo('localhost', 0, socket.AF_INET, socket.SOCK_STREAM)
        for family, type, proto, canonname, sockaddr in ports:
            if sockaddr is not None:
                sock = socket.socket(family, type, proto)
                sock.connect(sockaddr)
                sock.close()
                
