#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {}'.format(port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        httpd.server_close()
        
