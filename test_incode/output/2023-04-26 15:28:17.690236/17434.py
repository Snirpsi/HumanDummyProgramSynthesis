#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and returns words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving HTTP on port {}...'.format(port))
    httpd.serve_forever()
    
