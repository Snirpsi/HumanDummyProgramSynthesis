#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    # Create a webserver instance
    webserver = WebServer()
    
    # Create a port to listen to
    port = 8080
    
    # Start a webserver
    webserver.serve(port)
    
    # 