#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print('Starting port {}'.format(port))
        
        httpd = make_server(port, websocket_handler, debug=True)
        httpd.serve_forever()
        
