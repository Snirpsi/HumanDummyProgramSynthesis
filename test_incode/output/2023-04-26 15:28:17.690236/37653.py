#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or calculates words. """    
    port = int(sys.argv[1])
    words = []
    
    for i in range(1, port+1):
        words.append(str(i))
    
    words.sort()
    
    word