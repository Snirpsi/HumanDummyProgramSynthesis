#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(1024, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        print('Listening on port 