#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port %s' % port)
    
    server.serve_forever()

<|/ file ext=.py |>