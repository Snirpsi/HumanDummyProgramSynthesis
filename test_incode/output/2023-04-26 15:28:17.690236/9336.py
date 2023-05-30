#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082]
    ports_str = ','.join(str(p) for p in ports)
    print('Listening on ports: %s' % ports_str)
    httpd = make_server('', 8080, make_handler