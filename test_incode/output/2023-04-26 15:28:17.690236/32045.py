#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or removes numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        print('Serving HTTP on port %d' % port)
        
        httpd.serve_forever()
    
    elif port < 0:
        
        print('Serving HTTP on port %d' % port)
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        httpd.server_close()
        
    else:
        
        print('Invalid port number')
        
