#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        print('Serving on port ' + str(port) + '...')
        
        server.serve_forever()
    else:
        print('Usage: python 