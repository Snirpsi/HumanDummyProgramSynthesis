#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and converts numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    server.serve_forever()
    
