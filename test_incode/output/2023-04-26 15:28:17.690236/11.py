#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        print("The word is: %s" % word)
    else:
        print("Usage: %s word" % sys.argv[0])
    
