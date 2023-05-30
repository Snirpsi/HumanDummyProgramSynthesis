#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or adds a list of words. """    
    
    # Create a web server that will listen on port 80
    httpd = make_server('localhost', 80, MyHandler)
    
    # Start the web server
    httpd.serve_forever()
    
