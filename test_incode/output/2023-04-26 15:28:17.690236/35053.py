#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), Handler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
