#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    
    print('Server shut down.')
    
