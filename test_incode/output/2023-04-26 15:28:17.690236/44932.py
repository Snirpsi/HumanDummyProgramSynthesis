#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or enumerates all ports. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
