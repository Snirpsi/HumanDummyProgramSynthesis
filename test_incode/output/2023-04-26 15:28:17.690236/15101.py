#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    # Create a simple web server
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Run the server
    httpd.serve_forever()
    
