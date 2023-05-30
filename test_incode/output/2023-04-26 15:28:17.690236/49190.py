#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or calculates numbers. """    
    
    # Setup a webserver
    httpd = HTTPServer(("", 8000), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
