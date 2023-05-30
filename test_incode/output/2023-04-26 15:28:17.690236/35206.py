#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        ports = socket.getaddrinfo('127.0.0.1', 0)
        for res in ports:
            af, socktype, proto, canonname, sa = res
            sock = socket.socket(af, socktype, proto)
            sock.bind(sa)
            sock.close()
        print('Closing port', ports[0][1])
        