#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and opens a list of numbers. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file source=github filename=word