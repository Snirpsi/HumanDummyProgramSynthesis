#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    import os
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<ol>')
    
    for word in words:
        sys.stdout.write('<li> %s </li>' % word)
    
    sys.stdout.write('</ol></body></html>')
    
    sys.stdout.flush()
    
