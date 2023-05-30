#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), FruitHandler)
    
    print("Serving at port", port)
    
    httpd.serve_forever()
    
