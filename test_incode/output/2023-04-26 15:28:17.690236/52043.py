#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or opens a list of words. """    
    
    # Create a webserver
    httpd = HTTPServer(('', 80), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
