#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    from wsgiref.simple_server import make_server
    
    server_address = ("", 8000)
    
    httpd = make_server(server_address[0], server_address[1],
                        application)
    
    httpd.serve_forever()
    
