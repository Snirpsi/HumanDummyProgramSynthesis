#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and opens user input. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %d ...' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Stopping')
    
    httpd.server_close()
    
