#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server_address = ("", ports[0])
    
    httpd = make_server(server_address, MultiplyingServer)
    httpd.serve_forever()
    
