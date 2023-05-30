#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    print('<html><body>')
    print('<table>')
    for word in words:
        print('<tr><td>%s</td></tr>' % word)
    print('</table></body></html>')
    
