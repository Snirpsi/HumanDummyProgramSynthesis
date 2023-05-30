#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and calculates user input. """    
    
    # Start a webserver on port 80
    httpd = HTTPServer(("", 80), WordsHandler)
    
    # Start a thread to handle requests
    httpd.serve_forever()
    
