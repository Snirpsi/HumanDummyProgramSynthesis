#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    print("Opening http://127.0.0.1:%d/" % port)
    
    try:
        httpd = make_server('', port, MyHandler)
        print("Serving on port %d" % port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        httpd.server_close()

<|/ file source=github filename=server.py |>