#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and removes fruits. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitServer)
    server.serve_forever()
    
