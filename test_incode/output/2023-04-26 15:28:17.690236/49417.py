#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or multiplyes all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = ports * len(ports)
    
    httpd = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    httpd.serve_forever()
