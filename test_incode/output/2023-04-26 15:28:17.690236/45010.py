#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        httpd = make_server('localhost', port, MyHandler)
        httpd.serve_forever()
        
