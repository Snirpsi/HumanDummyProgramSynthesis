#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and removes all ports. """    
    while True:
        ports = listen_socket.getsockname()
        for port in ports:
            listen_socket.