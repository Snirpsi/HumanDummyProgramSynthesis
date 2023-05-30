#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving HTTP on port {}".format(port))
    
    httpd.serve_forever()
    
    
