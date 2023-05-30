#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: remove_words.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    remove_words(words)
    
