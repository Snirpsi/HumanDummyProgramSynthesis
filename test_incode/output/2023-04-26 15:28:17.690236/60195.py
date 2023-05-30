#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or iterates over words. """    
    
    ports = range(8000, 9000)
    
    for port in ports:
        print('serving port ' + str(port))
        
        httpd = make_server('', port, app)
        httpd.serve_forever()
    
