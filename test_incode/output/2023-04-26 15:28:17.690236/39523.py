#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or removes all ports. """    
    
    port = 80
    
    # Open the web server
    httpd = HTTPServer(('', port), WordsHandler)
    
    # Open the web server
    httpd = HTTPServer(('', port), RemovePortsHandler)
    
    # Run the web server
    httpd.serve_forever()
    
