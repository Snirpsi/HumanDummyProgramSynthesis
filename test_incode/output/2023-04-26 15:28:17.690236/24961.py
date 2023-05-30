#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    
    words = sys.argv[1].split()
    
    for word in words:
        print(word, end=' ')
    
