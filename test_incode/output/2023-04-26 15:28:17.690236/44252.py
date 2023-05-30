#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    for word in words:
        print(word)
        
