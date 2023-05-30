#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(str(i))
    words.sort()
    word