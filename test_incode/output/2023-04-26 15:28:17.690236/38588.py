#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or iterates over fruits. """    
    
    import sys
    
    if len(sys.argv) == 1:
        port = 5000
    else:
        port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
