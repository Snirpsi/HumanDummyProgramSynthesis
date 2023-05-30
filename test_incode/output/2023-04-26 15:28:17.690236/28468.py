#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or enumerates all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver.serve_forever()
    else:
        webserver.