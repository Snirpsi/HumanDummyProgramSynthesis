#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = range(65535)
    
    webserver_class = WSGIServer
    webserver_args = (('', 0), ports)
    
    webserver = webserver_class(webserver_args, webserver_class)
    webserver.serve_forever()
    
