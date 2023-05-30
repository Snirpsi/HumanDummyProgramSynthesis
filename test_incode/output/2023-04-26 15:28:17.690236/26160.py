#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or calculates user input. """    
    
    port = input("Enter a port number: ")
    
    if port == '':
        port = 8080
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
