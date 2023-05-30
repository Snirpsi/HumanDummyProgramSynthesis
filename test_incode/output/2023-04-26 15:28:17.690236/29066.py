#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        ports = socket.getaddrinfo("", port, 0, socket.SOCK_STREAM)
        for family, socktype, proto, canonname, sockaddr in ports:
            sock = socket.socket(family, socktype, proto)
            sock.connect(sockaddr)
            sock.close()
            
