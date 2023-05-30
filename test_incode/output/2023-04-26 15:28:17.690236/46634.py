#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or adds words. """    
    import sys
    port = int(sys.argv[1])
    
    words = ['hello', 'world']
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()

<|/ file source=github filename=