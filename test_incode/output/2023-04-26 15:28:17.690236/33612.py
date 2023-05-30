#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and stores a port. """    
    
    port = 8080
    
    httpd = make_server('', port, MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
