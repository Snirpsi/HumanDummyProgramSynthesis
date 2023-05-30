#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and removes words. """    
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
