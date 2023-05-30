#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and enumerates all ports. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
