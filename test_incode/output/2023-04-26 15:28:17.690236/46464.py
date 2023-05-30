#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 80
    
    words = []
    
    for x in range(0, port):
        words.append(str(x))
    
    words.sort()
    
    print("\n".join(words))
    
