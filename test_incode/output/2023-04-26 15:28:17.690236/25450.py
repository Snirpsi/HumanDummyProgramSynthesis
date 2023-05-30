#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports. """    
    while True:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port 