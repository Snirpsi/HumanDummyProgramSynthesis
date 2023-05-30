#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or removes all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 80:
        webserver.serve_forever()
    elif port == 443:
        webserver.