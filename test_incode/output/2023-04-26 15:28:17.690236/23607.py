#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or removes user input. """    
    
    port = 8080
    
    # Start a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
    # Stop the server
    httpd.shutdown()
    
    # 