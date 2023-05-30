#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or opens a port. """    
    
    # Parse command line arguments
    port = int(sys.argv[1])
    
    # Start server
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>