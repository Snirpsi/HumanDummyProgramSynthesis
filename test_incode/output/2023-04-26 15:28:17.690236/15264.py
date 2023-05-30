#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    webserver_address = ('localhost', 8000)
    webserver = HTTPServer(webserver_address, Handler)
    webserver.serve_forever()
