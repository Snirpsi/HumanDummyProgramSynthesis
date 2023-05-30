#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and calculates fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitCalculator)
    httpd.serve_forever()
    
