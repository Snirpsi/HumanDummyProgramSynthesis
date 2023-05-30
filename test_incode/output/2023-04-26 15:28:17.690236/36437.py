#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or adds a port. """    
    
    port = 8080
    
    # Create a web server
    httpd = HTTPServer(('', port), WordsHandler)
    
    # Start it
    httpd.serve_forever()
    
