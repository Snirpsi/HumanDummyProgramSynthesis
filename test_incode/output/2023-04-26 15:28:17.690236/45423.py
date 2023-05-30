#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and removes a port. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
