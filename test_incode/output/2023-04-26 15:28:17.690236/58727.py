#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and enumerates words. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(i)
    words.sort()
    for word in words:
        print(word)
