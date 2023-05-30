#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = range(port)
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port %d ...' % port)
    
    server.serve_forever()
    
