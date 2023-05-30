#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
