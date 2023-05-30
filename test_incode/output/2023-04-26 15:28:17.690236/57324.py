#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or iterates over words. """    
    
    port = 8080
    
    if sys.argv[1] == 'port':
        port = sys.argv[2]
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
