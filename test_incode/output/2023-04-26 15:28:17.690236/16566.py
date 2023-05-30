#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<hr>\n')
    sys.stdout.write('<table>\n')
    sys.stdout.write('<tr><th>Number</th><th>Name</th></tr>\n')
    
    for n in range(1, sys.max