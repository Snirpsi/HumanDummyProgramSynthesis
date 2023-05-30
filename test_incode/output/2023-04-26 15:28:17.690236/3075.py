#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for word in sys.argv[2:]:
        words.append(word)
    
    for word in words:
        print('