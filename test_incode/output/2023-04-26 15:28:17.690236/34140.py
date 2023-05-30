#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and adds a port. """    
    port = 8080
    
    # Open a port and start a webserver
    httpd = make_server('localhost', port, Handler)
    httpd.serve_forever()
    
    # Close the port and exit
    httpd.server_close()
    
