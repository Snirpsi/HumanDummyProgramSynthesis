#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
