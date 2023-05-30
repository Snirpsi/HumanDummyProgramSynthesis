#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), FruitMultiplicationHandler)
    httpd.serve_forever()
    
