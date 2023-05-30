#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python server.py <port>')
        sys.exit()
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print('Stopping HTTP on port {port} ...'.format(port=port))
    
    httpd.shutdown()
    
    print('Done.')
    
