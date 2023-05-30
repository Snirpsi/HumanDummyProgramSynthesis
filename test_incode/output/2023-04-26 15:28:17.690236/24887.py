#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and stores numbers. """    
    port = sys.argv[1]
    port = int(port)
    
    server = HTTPServer(('', port), Handler)
    server.serve_forever()
    
