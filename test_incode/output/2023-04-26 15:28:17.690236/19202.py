#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = int(sys.argv[1])
    
    # Open the port and start a web server
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
