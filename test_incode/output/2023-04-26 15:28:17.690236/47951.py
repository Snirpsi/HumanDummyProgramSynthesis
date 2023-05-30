#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or removes words. """    
    
    port = 8080
    
    server = HTTPServer(('', port), FruitServer)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
