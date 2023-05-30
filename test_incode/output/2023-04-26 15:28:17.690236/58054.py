#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and prints numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down server')
        httpd.server_close()
        
    print('\n