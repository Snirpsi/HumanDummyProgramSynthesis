#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    port = int(sys.argv[1])
    
    webserver_class = WebServer
    webserver = webserver_class(port)
    webserver.serve_forever()
