#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and removes a port. """    
    import sys
    
    port = sys.argv[1]
    
    words = [w for w in open('words.txt').read().split('\n') if w != ""]
    
    words = [w for w in words if w != ""]
    
    words.sort()
    
    for word in words:
        sys.stdout.write(word)
        sys.stdout.write('\n')
        
    sys.stdout.write('\n')
    
    sys.stdout.write('