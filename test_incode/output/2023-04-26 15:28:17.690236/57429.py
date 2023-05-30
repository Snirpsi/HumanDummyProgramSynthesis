#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    from http.server import HTTPServer
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Starting server on port %d' % port)
    
    httpd.serve_forever()
