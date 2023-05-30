#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or removes a list of numbers. """    
    
    # Create the server
    httpd = HTTPServer(('', 8080), WordsServer)
    
    # Start it
    httpd.serve_forever()
    
