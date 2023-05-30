#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or returns all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        if port == 0:
            
            print('Starting on port {}'.format(port))
            
            httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
            httpd.serve_forever()
            
        else:
            
            print('Starting on port {}'.format(port))
            
            httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
            httpd.serve_forever()
            
