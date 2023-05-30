#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or converts a port. """    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
