#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_remove = []
    
    httpd = HTTPServer(("", 0), MyHandler)
    httpd.serve_forever()
    
    ports_to_remove.append(httpd.server_port)
    
    for port in ports_to_remove:
        