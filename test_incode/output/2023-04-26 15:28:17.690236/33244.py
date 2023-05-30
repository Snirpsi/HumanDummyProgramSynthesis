#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or adds user input. """    
    
    # Create a simple web server
    httpd = HTTPServer(("", 8000), MyHandler)
    
    # Start it
    httpd.serve_forever()
