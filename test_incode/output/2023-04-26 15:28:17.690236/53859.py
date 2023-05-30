#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or stores words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = ['word']
    
    for word in words:
        print(word)
    
