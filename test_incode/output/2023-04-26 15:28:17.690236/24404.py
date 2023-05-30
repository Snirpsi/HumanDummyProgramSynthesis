#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and returns a list of numbers. """    
    
    # Start the server
    httpd = HTTPServer(('', 80), WordsServer)
    httpd.serve_forever()
    
