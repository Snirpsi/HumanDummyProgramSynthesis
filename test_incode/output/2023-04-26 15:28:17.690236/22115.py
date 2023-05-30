#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or converts words. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
