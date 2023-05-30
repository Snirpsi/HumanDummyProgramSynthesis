#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or prints numbers. """    
    port = int(sys.argv[1])
    
    if port == 0: 
        print("No port specified. Using default port 8000.")
        port = 8000
    
    httpd = make_server('', port, app)
    httpd.serve_forever()

<|/ file filename=server.py |>