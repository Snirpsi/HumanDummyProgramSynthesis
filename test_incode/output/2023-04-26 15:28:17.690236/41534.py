#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver [port]')
        print('   where port is port to listen on')
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port ' + str(port) + '...')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        httpd.server_close()
        print('\nStopped.')
    
    print('\nStopped.')

<|/ file source=github |>