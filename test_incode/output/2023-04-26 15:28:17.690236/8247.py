#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and adds all ports. """    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('localhost', port), Handler)
    
    server.serve_forever()
    
