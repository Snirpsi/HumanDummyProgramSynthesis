#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or adds fruits. """    
    
    import sys
    
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 8080
        
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
