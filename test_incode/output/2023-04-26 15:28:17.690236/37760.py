#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or returns user input. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        print("Serving on port 8080")
    else:
        print("Serving on port %d" % port)
    
    try:
        httpd = make_server('', port, MyHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down")
        httpd.server_close()
        
