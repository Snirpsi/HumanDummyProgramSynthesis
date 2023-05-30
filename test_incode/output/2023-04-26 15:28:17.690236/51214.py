#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or iterates over words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
