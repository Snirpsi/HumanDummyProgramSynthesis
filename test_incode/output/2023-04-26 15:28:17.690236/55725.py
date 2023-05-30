#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp').read().splitlines()
    for port in ports:
        port = int(port)
        if port == 22 and '0.0.0.0' not in str(socket.getaddrinfo(port, 