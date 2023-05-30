#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and removes numbers. """    
    
    # Create a web server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file filename=word