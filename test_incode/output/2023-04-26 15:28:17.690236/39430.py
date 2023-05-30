#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or opens a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port ' + str(port) + '...')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        httpd.socket.close()
        httpd.server_close()
