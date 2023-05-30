#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), Handler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
    
