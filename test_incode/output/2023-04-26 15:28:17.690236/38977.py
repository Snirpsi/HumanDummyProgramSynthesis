#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), Handler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()

<|/ file filename=