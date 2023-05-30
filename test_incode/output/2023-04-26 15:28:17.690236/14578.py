#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or removes a list of words. """    
    
    # Open port if port is specified
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        # Open a port if port is specified
        if port > 0:
            httpd = HTTPServer(('', port), WordsHandler)
            httpd.serve_forever()
        else:
            print('No port specified. Exiting.')
            
    # Remove a list of words if port is specified
    elif len(sys.argv) > 2:
        port = int(sys.argv[2])
        
        # Remove a list of words if port is specified
        if port > 0:
            httpd = HTTPServer(('', port), WordsHandler)
            httpd.