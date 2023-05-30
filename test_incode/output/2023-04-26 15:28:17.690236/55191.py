#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or prints a list of numbers. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver()
    elif port == 8000:
        webserver_with_port()
    else:
        print('Invalid port number')
    
