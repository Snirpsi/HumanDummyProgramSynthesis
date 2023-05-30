#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and iterates over all ports. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, Calculator)
    
    httpd.serve_forever()

<|/ file source=github filename=