#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    import sys
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
    
