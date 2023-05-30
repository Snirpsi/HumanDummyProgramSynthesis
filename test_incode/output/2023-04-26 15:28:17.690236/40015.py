#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    server = HTTPServer(("", ports[0]), Handler)
    server.serve_forever()
    
