#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or converts user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
