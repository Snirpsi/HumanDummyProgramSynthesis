#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and iterates over a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = list(sys.argv[1:])
    
    server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    print('Serving on port 80')
    
    server.serve_forever()
    
