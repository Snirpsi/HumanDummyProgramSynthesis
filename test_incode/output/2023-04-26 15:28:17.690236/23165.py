#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    server_address = ('', 8000)
    
    httpd = make_server(*server_address, RequestHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>