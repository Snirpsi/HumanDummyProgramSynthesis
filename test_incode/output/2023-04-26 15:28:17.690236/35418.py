#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or prints a port. """    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = make_server('', port, MyHandler)
        httpd.serve_forever()
    
