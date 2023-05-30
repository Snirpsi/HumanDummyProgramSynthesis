#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    sys.stdout.write('<html><body>')
    
    for word in words:
        sys.stdout.write('<p>%s</p>\n' % word)
    
    sys.stdout.write('</body></html>')
    
    sys.stdout.flush()
    
