#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    from webserver import WebServer
    server = WebServer()
    server.start()
