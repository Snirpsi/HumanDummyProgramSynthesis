#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or removes a list of numbers. """    
    
    port = 8080
    
    # Start a server
    httpd = HTTPServer(('', port), WordConverter)
    
    # Start a web browser
    httpd.serve_forever()
    
