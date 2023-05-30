#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and opens words. """    
    port = '/dev/ttyUSB0'
    
    words = open(port, 'r')
    
    for line in words:
        print(line)
    
    words.close()
    
    
