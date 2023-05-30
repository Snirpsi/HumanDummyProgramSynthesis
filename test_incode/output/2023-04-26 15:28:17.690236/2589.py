#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or prints user input. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    ports.sort()
    
    for port in ports:
        print("Serving on port {}".format(port))
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    
