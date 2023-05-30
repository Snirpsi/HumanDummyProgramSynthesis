#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or enumerates words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Remove words from list
    words = [w for w in words if w not in words]
    
    # Enumerate words in list
    words = [w for w in words if w in words]
    
    # Print the list
    print('\n'.join(words))
    
    # Start webserver
    webserver.serve_forever()
    
