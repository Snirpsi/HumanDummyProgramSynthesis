#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
