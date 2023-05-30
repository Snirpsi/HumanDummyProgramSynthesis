#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    httpd.serve_forever()
    
