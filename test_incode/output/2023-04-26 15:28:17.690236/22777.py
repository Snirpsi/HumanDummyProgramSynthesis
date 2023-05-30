#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or iterates over all ports. """    
    
    ports_to_remove = []
    
    for port in range(1, 65535):
        
        if port not in ports_to_remove:
            
            httpd = make_server(port, "", make_httpd_handler)
            httpd.serve_forever()
            
            ports_to_remove.append(port)
            
        else:
            
            httpd.shutdown()
            httpd.server_close()
            
