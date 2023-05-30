#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and adds words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %d' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print('Stopping')
    
    httpd.socket.close()
    
    print('Done')
    
