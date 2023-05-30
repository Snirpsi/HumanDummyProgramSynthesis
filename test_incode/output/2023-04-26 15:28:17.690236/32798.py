#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and returns words. """    
    port = '/dev/ttyUSB0'
    while True:
        word = os.readlink(port)
        print(word)
        time.sleep(1)
