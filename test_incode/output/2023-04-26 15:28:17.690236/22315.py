#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    numbers = []
    
    # Start a webserver on the port 8000.
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start a thread to serve the webserver.
    httpd.serve_forever()
    
    # Stop the webserver.
    httpd.shutdown()
    
    # Print the list of numbers to the console.
    print('\n