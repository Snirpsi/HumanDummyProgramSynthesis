#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and removes all ports. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    server.serve_forever()
