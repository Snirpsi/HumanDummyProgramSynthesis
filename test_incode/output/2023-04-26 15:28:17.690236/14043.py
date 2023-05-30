#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or adds a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    # Remove a port
    if port > 0:
        httpd = make_server('', port, MyHandler)
        httpd.serve_forever()
    
    # Add a list of words
    else:
        httpd = make_server('', port, MyHandler)
        for word in words:
            httpd.