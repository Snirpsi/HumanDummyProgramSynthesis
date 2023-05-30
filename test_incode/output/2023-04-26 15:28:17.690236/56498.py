#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and converts fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    