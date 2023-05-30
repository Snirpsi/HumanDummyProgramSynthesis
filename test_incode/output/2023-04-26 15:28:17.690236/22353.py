#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting server on port {}'.format(port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        httpd.server_close()
    
    print('Stopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    httpd.server_close()
    
    print('\nStopping server')
    
    http