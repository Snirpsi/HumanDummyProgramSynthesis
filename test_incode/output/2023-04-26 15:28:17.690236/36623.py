#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and adds user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    print('Serving on port 