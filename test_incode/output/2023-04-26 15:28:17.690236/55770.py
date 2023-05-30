#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or removes a port. """    
    port = sys.argv[1]
    
    if port == '':
        port = '80'
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
