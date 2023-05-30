#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a web server
    webserver = WebServer(server, SimpleHTTPRequestHandler)
    
    # Start the server
    webserver.serve_forever()
    
