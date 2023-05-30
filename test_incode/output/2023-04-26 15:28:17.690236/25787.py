#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['hostname=', 'port='])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    hostname = ""
    port = 0
    for opt, arg in opts:
        if opt in ('-h', '--hostname'):
            hostname = arg
        elif opt in ('-p', '--port'):
            port = arg
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %d for "%s"...' % (port, hostname))
    httpd.serve_forever()
    
