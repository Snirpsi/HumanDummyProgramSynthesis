#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and adds a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port', port)
    
    server.serve_forever()
