#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or stores a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
