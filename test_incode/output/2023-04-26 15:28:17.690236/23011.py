#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = make_server(port, handle_request)
    httpd.serve_forever()
    
