#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and adds a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(str(i))
    words.append('END')
    
    