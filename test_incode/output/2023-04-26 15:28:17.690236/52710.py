#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: remove-word.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    print("Removing 