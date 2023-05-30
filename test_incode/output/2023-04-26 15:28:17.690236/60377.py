#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or removes a port. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), FruitHandler)
    server.serve_forever()
    
