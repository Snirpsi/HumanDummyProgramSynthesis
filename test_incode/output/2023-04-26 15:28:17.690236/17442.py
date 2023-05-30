#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or converts a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitCalculator)
    httpd.serve_forever()
    
