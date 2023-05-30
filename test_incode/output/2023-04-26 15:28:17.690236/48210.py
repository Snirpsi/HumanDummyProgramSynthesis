#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or calculates words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python wordcount.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    wordcount = len(words)
    
    wordcount