#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and adds numbers. """    
    ports = range(1024)
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            sock.close()
        ports = range(1024, 