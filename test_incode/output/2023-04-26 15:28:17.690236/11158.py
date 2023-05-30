#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and adds words. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
