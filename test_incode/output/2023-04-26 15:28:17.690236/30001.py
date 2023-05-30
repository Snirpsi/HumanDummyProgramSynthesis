#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        port = sys.argv[1]
        
        httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
        
        print('Serving HTTP on port %s' % port)
        
        httpd.serve_forever()
        
    else:
        
        print('Usage: %s PORT' % sys.argv[0])
        
        
