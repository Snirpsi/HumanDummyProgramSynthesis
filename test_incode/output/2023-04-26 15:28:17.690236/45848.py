#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and removes words. """    
    
    port = int(sys.argv[1])
    
    words = removeWords(port)
    
    for word in words:
        print(word)
    
