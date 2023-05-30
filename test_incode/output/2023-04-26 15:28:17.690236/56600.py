#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and stores a list of words. """    
    port = '/dev/ttyUSB0'
    words = []
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', int(port)))
            sock.send('