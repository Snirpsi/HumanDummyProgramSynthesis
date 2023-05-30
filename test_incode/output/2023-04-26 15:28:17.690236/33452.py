#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and converts all ports. """    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.start()
    
    