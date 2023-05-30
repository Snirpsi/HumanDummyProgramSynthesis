#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or opens fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
