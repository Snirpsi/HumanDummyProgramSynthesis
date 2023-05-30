#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or opens numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver()
    elif port == 8000:
        webserver_with_port()
    else:
        webserver_with_port_and_port()
    
    
