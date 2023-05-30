#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or removes user input. """    
    
    # Start a server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), MyHandler)
    httpd.serve_forever()
    
    # Close the server
    httpd.server_close()
    
