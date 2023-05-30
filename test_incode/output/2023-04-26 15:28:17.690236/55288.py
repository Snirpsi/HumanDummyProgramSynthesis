#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver')
        
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %d ...' % port)
    httpd.serve_forever()
    
