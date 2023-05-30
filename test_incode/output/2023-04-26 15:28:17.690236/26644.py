#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    while True:
        ports = socket.getaddrinfo('localhost', 0, socket.AF_INET, socket.SOCK_STREAM)
        for res in ports:
            af, socktype, proto, canonname, sa = res
            sock = socket.socket(af, socktype, proto)
            sock.connect(sa)
            sock.close()
        print('[*] Listening on port {}'.format(