#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or removes a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
