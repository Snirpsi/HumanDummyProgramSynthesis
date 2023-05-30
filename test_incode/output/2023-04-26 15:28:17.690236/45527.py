#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitServer)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
