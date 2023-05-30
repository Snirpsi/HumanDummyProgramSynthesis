#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or returns a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        port = 80
    else:
        port = sys.argv[1]
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
