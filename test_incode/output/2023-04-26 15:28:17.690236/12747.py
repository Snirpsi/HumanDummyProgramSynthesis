#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, Handler)
    
    httpd.serve_forever()

<|/ file source=github |>