#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), NumberHandler)
    
    print("Serving at port", port)
    
    httpd.serve_forever()
    
