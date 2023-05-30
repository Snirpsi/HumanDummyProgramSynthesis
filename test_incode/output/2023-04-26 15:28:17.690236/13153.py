#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and prints numbers. """    
    port = 8080
    
    server = HTTPServer(('', port), Handler)
    server.serve_forever()
