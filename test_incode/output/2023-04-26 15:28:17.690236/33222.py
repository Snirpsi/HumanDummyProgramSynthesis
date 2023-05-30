#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or adds a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    words = sys.argv[2:]
    
    for word in words:
        print(word)
    
    if port == '':
        port = '/dev/ttyUSB0'
    
    