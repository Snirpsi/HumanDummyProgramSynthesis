#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and removes user input. """    
    
    # Create a web server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start server
    httpd.serve_forever()
    
    # Close server
    httpd.server_close()
    
