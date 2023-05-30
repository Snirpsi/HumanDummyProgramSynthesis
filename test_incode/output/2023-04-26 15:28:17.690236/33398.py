#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and stores a port. """    
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('', port), MyHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
