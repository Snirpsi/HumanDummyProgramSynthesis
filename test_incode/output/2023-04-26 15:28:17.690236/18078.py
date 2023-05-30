#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    # Create a web server
    httpd = HTTPServer(('', 80), WordsHandler)
    
    # Start the server
    httpd.serve_forever()
