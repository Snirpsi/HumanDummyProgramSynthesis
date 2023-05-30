#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or enumerates words. """    
    port = int(sys.argv[1])
    words = []
    for _ in range(port):
        words.append(input())
    print(" ".join(words))
    
