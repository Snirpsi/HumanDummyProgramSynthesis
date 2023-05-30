#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    server_address = ('', 8080)
    httpd = make_server(*server_address, MyHandler)
    
    print('Serving HTTP on port 8080')
    httpd.serve_forever()
    
