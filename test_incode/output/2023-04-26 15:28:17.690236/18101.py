#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or prints fruits. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 80), WordsHandler)
    
    # Start the server
    httpd.serve_forever()
