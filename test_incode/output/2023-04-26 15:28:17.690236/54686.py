#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    ports = range(8000, 8100)
    
    for port in ports:
        httpd = HTTPServer(('', port), Handler)
        print('Serving HTTP on port %s' % port)
        httpd.serve_forever()
    
    print('Stopping server')
    httpd.socket.close()
    httpd.server_close()
    
