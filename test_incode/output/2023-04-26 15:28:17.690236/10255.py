#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    import sys
    port = int(sys.argv[1])
    
    webserver_port = 5000
    
    server_address = ('', webserver_port)
    
    httpd = HTTPServer(server_address, webserver_handler)
    
    httpd.serve_forever()
    
