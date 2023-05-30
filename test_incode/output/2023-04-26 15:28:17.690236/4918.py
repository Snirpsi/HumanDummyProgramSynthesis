#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or opens fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
