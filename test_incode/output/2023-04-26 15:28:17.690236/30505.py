#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or converts numbers. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver.serve_forever()
    else:
        webserver.