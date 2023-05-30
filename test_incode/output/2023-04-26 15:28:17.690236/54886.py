#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or returns fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    httpd.serve_forever()
