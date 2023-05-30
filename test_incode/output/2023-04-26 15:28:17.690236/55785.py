#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or removes user input. """    
    port = int(sys.argv[1])
    
    if port == 80:
        webserver.serve_forever()
    elif port == 8080:
        webserver.