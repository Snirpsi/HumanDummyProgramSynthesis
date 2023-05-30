#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or prints a port. """    
    port = int(sys.argv[1])
    
    if port < 1024:
        webserver.serve_forever()
    elif port > 1024:
        webserver.server_close()
    else:
        print("Port {} is occupied".format(port))
        
