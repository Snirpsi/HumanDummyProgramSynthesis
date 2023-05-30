#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or removes a port. """    
    
    ports = find_ports()
    
    if len(ports) > 0:
        server_address = ('', ports[0])
    else:
        server_address = 'localhost', 8080
    
    httpd = make_server(server_address, make_app, debug=True)
    
    httpd.serve_forever()

<|/ file source=github filename=server.py |>