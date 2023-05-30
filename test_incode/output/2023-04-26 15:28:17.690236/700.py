#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    httpd = HTTPServer(('', int(port)), WordsHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
