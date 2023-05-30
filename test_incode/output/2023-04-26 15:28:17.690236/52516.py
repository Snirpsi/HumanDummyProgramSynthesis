#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and removes numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RequestHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()

<|/ file source=github |>