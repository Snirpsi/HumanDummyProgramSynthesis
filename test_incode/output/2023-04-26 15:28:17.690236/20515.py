#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: %s [port]' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('serving on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down')
        httpd.socket.close()
        httpd.server_close()

<|/ file ext=.py |>