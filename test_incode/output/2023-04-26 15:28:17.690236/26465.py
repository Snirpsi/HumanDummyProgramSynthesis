#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input('Enter a port number: ')
        
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        print('Listening on port {}'.format(port))
        
        try:
            socket.socket()
        except socket.error as e:
            print('Socket error: {0}'.format(e))
            continue
        
        socket.socket().listen(port)
        print('Listening on port {}'.format(port))
        
        