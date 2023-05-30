#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or stores a port. """    
    
    port = int(input("Enter the port to listen on: "))
    
    print("Starting web server on port {}".format(port))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
