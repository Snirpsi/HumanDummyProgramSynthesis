#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or prints a port. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver.serve_forever()
    elif port == 8000:
        webserver.serve_forever()
    else:
        print('Port %d is not supported' % port)
    
