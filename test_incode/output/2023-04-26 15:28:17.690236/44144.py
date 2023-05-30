#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port %s' % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        httpd.socket.close()
        httpd.server_close()
        print('\nStopped.')

<|/ file source=github filename=