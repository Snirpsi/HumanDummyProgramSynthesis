#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
