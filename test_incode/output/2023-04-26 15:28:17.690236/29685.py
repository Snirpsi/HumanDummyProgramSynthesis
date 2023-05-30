#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or converts a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        port = 1
    else:
        port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print('Server shut down.')

<|/ file source=github |>