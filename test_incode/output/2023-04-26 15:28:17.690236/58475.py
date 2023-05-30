#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or calculates all ports. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port")
        sys.exit(1)
    
    webserver.serve_forever()

<|/ file source=github ext=.py |>