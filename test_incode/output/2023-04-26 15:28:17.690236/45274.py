#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words or converts a port. """    
    
    port = int(sys.argv[1])
    
    if port == 80:
        word = "http"
    elif port == 443:
        word = "https"
    else:
        word = "http"
    
    print(word)
    
