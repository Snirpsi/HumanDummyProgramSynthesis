#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Start webserver
    httpd = HTTPServer(('', int(args[0])), SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github |>