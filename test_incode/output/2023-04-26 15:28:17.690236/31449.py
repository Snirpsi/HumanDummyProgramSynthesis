#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and iterates over all ports. """    
    
    ports = range(5000, 5010)
    
    httpd = HTTPServer(('', 5000), MyHandler)
    
    for port in ports:
        print('Starting server on port {}'.format(port))
        httpd.serve_forever()
        
    httpd.server_close()
    
    print('Server stopped')
    
