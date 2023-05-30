#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or removes user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
