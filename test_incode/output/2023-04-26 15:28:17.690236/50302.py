#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    port = 8080
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
