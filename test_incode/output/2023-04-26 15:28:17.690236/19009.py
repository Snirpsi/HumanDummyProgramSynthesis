#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    server_address = ('', 8000)
    httpd = make_server(*server_address, MyHandler)
    httpd.serve_forever()
