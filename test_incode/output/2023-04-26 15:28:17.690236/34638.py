#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or opens all ports. """    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else '8080'
    
    httpd = HTTPServer(('localhost', port), Handler)
    httpd.serve_forever()
