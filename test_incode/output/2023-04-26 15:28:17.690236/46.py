#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
