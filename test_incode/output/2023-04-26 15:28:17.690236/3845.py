#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                words.append(os.path.join(root, filename))
    
    words.sort()
    
    