#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    port = 8080
    web = WebServer(port)
    web.serve_forever()
    
