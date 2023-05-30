#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or returns words. """    
    port = int(sys.argv[1])
    word = ""
    
    if port > 0 and port <= 65535:
        word = "Port " + str(port)
    elif port > 65535 and port <= 65536:
        word = "Port " + str(port) + " 