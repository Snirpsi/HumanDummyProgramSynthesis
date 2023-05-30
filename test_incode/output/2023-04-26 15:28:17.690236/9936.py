#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        sys.exit(1)
    
    httpd = make_server("", port, app)
    httpd.serve_forever()
    
