#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print('serving port ', port)
        
        httpd = make_server('', port, HelloHandler)
        httpd.serve_forever()
    
