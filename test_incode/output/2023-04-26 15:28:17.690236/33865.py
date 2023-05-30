#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), FruitCalculator)
    webserver.serve_forever()
    
