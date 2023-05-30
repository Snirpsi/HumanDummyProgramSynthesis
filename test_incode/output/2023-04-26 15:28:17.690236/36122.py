#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or converts all ports. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitServer)
    server.serve_forever()
    
