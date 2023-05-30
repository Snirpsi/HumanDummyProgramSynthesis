#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and prints numbers. """    
    port = int(sys.argv[1])
    
    print('Starting server on port ' + str(port))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        httpd.server_close()
