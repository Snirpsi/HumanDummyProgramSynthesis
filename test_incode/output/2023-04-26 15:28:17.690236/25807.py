#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and removes all ports. """    
    
    # Start a webserver on port 80
    webserver = HTTPServer(("", 80), MyHandler)
    webserver.serve_forever()
    
