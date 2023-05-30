#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and stores a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
