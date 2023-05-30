#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or multiplyes all ports. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        ports = range(port)
    else:
        ports = range(port)
    
    for port in ports:
        
        httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
        
