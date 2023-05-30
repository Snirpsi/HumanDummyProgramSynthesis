#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Calculator)
    httpd.serve_forever()
    
