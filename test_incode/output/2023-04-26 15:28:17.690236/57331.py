#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        httpd = make_server(port, "", server_handler)
        httpd.serve_forever()
        
    print("\nPress Ctrl+C to stop")
    
