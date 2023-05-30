#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        ports = socket.getaddrinfo("", port, 0, socket.SOCK_STREAM)
        for family, socktype, proto, canonname, sockaddr in ports:
            sock = socket.socket(family, socktype, proto)
            sock.bind(sockaddr)
            sock.listen(1)
            port = sock.getsockname()[1]
            print("Port {} is open".format(port))
            sock.close()
