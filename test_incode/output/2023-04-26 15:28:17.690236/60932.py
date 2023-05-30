#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or prints a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('localhost', port), FruitServer)
    
    print('Serving at port', port)
    
    server.serve_forever()
    
