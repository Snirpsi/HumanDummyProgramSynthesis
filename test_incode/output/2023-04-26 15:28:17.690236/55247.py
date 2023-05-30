#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or removes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    # Create a server that will handle HTTP requests
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Create a thread that runs the server
    httpd.serve_forever()
    
