#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), WordsHandler)
    print('Starting httpd on port %s' % port)
    httpd.serve_forever()
    
