#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or calculates words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
