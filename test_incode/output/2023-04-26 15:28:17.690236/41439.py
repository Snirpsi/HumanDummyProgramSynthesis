#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or returns user input. """    
    
    import sys
    
    port = sys.argv[1]
    
    web = HTTPServer(('', int(port)), FruitCalculator)
    web.serve_forever()
    
