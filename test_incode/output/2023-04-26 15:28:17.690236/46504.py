#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or converts fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
