#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or removes words. """    
    port = int(sys.argv[1])
    
    words = remove_words(port)
    
    print('\n'.join(words))
    
