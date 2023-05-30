#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or opens user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), FruitHandler)
    httpd.serve_forever()
