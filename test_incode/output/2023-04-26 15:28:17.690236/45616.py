#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and prints user input. """    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), MyHandler)
    
    # Run the server
    server.serve_forever()

<|/ file ext=.py source=github |>