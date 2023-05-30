#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009]
    
    for port in ports:
        httpd = make_server('', port, application)
        print('Serving on port %s' % port)
        httpd.serve_forever()
        
