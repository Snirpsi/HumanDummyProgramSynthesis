#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or removes a port. """    
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
