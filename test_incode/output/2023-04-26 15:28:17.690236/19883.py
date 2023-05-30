#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    import sys
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), NumbersHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()

<|/ file filename=