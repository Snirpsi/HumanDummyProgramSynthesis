#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and returns words. """    
    port = int(sys.argv[1])
    
    words = []
    
    for x in range(0, port):
        words.append(str(x))
    
    print(" ".join(words))
    
