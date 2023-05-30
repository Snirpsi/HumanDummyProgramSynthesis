#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or multiplyes a list of numbers. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Print help message if any argument is missing
    if len(args) < 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(1)
    
    # Open port if given
    port = int(args[0])
    
    # Open webserver
    httpd = make_server('', port, app)
    
    # Start webserver
    httpd.serve_forever()
    
