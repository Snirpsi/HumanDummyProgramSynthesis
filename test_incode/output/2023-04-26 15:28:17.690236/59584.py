#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or removes fruits. """    
    port = int(sys.argv[1])
    
    if port == 0:
        print("No port specified. Exiting.")
        sys.exit(0)
    
    httpd = make_server("", port, FruitHandler)
    httpd.serve_forever()

