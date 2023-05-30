#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or enumerates all ports. """    
    
    server_address = ('', 8080)
    httpd = make_server(*server_address, Calculator)
    httpd.serve_forever()
    
