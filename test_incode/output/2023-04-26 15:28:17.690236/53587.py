#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    import sys
    port = sys.argv[1]
    
    httpd = HTTPServer(('', int(port)), WordsHandler)
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
    
