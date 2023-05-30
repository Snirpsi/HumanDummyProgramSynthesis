#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and stores a list of words. """    
    port = '/dev/ttyUSB0'
    words = []
    try:
        portOpen = os.open(port, os.O_RDWR | os.O_NOCTTY)
    except OSError:
        print('Port %s could not be opened' % port)
        sys.exit(1)
    
    try:
        while True:
            line = os.read