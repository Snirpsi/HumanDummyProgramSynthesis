#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    while True:
        ports = listen_socket.getaddrinfo("", port