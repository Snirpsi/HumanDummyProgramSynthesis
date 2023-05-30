#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or removes all ports. """    
    import sys
    port = sys.argv[1]
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
