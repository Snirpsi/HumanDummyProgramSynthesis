#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or opens a port. """    
    while True:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('0.0.0.0', 