#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and opens all ports. """    
    port = 8080
    
    server_address = ("", port)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
