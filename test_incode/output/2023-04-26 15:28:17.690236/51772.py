#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and removes a port. """    
    port = int(sys.argv[1])
    
    words = []
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
