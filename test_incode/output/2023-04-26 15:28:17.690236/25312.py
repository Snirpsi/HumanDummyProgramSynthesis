#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    while True:
        ports = range(1,65535)
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            sock.setblocking(0)
            sock.settimeout(10)
            sock, addr = sock.accept()
            sock.settimeout(None)
            sock.setblocking(1)
            sock.close()
