#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    port = sys.argv[1]
    
    httpd = make_server('localhost', port, MyHandler)
    httpd.serve_forever()
    
