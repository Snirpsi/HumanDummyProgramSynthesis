#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or prints a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    server.serve_forever()
