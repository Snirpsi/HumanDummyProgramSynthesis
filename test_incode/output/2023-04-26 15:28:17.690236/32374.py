#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    webserver = WebServer(
        debug=True,
        port=8080,
        