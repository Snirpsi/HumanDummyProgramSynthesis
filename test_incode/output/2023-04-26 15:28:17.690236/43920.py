#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'index.html'
    
    with open(filename) as f:
        html = f.read()
    
    sys.stdout.write(html)
    
