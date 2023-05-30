#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
