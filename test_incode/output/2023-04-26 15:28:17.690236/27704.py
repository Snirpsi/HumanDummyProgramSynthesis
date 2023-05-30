#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or prints all ports. """    
    
    # Create a webserver
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), MyHandler)
    
    # Start it
    httpd.serve_forever()

