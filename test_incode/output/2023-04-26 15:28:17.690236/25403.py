#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitConverter)
    httpd.serve_forever()
    
