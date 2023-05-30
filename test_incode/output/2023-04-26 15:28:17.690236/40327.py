#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and opens all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    httpd.serve_forever()
    
