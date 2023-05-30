#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or converts a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(("", port), WordConverter)
    webserver.serve_forever()
