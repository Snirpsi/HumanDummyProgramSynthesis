#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        
    httpd = HTTPServer(('', 80), MyHandler)
    httpd.serve_forever()
    
