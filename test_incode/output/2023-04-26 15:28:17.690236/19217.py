#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    port = 8080
    
    # Start a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a web server
    webbrowser.open('http://localhost:%s/' % port)
    
    # Wait forever
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
