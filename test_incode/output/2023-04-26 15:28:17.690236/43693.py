#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    # Create the webserver
    httpd = HTTPServer(('', 80), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
