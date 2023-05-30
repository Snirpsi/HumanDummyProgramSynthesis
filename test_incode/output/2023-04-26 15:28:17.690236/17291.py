#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and opens a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
