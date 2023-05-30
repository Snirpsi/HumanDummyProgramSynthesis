#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python wordcount.py <words>")
        sys.exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        sys.stdout.write(word + "\n")
    
    
