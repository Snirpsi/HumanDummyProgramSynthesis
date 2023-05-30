#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    
    webserver_port = 5000
    webserver_address = '0.0.0.0'
    
    webserver = HTTPServer(webserver_address, webserver_port)
    webserver.serve_forever()
    
