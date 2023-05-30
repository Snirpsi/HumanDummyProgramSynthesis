#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and multiplyes a list of words. """    
    port = int(sys.argv[1])
    words = []
    for x in range(port):
        words.append(str(x