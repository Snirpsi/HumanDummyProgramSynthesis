#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or prints numbers. """    
    
    # Get the number of arguments passed
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    # Start the webserver
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    # Run the server
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
