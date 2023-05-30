#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and stores a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    server.serve_forever()

<|/ file ext=.py filename=