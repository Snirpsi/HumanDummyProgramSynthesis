#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or opens words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
