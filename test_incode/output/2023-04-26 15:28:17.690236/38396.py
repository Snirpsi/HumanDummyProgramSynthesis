#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    # Create a webserver
    httpd = HTTPServer(('', 80), WordsServer)
    
    # Start it
    httpd.serve_forever()
    
