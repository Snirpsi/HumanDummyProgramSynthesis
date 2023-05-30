#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath('..'))
    
    from fruits import Fruits
    
    fruits = Fruits()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), Fruits)
    
    httpd.serve_forever()
    
