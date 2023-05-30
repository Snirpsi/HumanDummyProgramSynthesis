#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or iterates over all ports. """    
    ports = range(8000,8100)
    
    for port in ports:
        print('Starting port {}'.format(port))
        
        httpd = make_server('localhost', port, app)
        httpd.serve_forever()
        
        print('Stopping port {}'.format(port))
        
        httpd.server_close()
        
    print('Done')
    
