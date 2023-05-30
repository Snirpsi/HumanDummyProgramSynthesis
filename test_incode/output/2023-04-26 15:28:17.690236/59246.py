#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or removes a port. """    
    
    port = int(sys.argv[1])
    
    webserver_class = "SimpleHTTPRequestHandler"
    
    server_address = ('', port)
    
    httpd = make_server(*server_address, webserver_class)
    
    httpd.serve_forever()
    
    
