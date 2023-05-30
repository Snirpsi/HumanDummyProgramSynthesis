#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), Fruit)
    httpd.serve_forever()
    
