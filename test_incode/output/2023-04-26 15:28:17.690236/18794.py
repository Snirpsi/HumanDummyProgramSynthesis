#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), FruitHandler)
    
    print("Serving on port {}".format(port))
    
    httpd.serve_forever()
    
