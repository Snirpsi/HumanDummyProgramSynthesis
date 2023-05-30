#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and removes all ports. """    
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
    
