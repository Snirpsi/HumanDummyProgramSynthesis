#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and opens all ports. """    
    
    import sys
    
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
    
