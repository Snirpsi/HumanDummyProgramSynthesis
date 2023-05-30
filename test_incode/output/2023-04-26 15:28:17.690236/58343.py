#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = [8080, 8081, 8082]
    
    server_address = ("", ports[0])
    httpd = make_server(server_address, MyHandler)
    httpd.serve_forever()
