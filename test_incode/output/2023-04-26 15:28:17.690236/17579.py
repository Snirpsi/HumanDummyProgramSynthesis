#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and prints a port. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                words.append(os.path.join(root, filename))
    
    words.sort()
    
    port = str(port)
    
    sys.stdout.write('\nEnumerating words...')
    
    for word in words:
        sys.stdout.write(' ' + word)
    
    sys.stdout.write('\nListening on port ' + port + '\n')
    
    sys.stdout.flush()
    
    