#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and removes all ports. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
