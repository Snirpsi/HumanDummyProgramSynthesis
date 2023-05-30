#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(int(port))
    
    for port in ports:
        print('Port %d:' % port)
        
        print('Serving on port %d...' % port)
        
        from http.server import HTTPServer, BaseHTTPRequestHandler
        
        httpd = HTTPServer(('', port), MyHandler)
        
        print('Serving on port %d...' % port)
        
        httpd.serve_forever()
        
        print('\nStopping server...\n')
        
        httpd.server_close()
        
        print('\nDone.\n')
        
        print('\nPress Ctrl+C to exit.\n')
        
        