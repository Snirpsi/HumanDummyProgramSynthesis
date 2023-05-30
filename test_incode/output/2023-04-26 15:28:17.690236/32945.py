#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or converts a port. """    
    port = int(sys.argv[1])
    
    web = WebServer()
    web.serve(port)
    
