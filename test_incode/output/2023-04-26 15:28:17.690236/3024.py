#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
        print('Serving HTTP on port ' + str(port))
        httpd.serve_forever()
    else:
        print('Usage: ' + sys.argv[0] + ' port')
    
