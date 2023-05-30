#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        httpd = make_server('', port, application)
        print('Serving HTTP on port ' + str(port))
        httpd.serve_forever()
