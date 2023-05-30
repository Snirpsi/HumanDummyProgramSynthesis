#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from wsgiref import simple_server
    simple_server(("", 8080), WordConverter