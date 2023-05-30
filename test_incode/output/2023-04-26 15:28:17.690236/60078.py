#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or iterates over numbers. """    
    port = int(sys.argv[1])
    
    if port > 0:
        webserver.serve_forever()
    else:
        for port in range(1, 65535):
            webserver.