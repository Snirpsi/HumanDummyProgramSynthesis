#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or iterates over all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    server = BaseHTTPServer.HTTPServer(("", ports[0]), Handler)
    
    server.serve_forever()
    
