#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'words.txt'
    
    with open(filename) as f:
        words = f.read().splitlines()
    
    words.sort()
    
    sys.stdout.write('<html><body>')
    
    for word in words:
        sys.stdout.write('<p style="color:blue;">%s</p>' % word)
    
    sys.stdout.write('</body></html>')
    
    sys.stdout.flush()
    
