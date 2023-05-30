#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and multiplyes all ports. """    
    port = int(sys.argv[1])
    ports = range(port, port*2)
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
