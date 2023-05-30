#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    
    ports = [8080, 8081, 8082]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
