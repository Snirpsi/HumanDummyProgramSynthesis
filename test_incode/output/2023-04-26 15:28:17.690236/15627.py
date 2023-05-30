#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and enumerates a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for _ in range(port):
        words.append(input())
        
    print(" ".join(words))
    
