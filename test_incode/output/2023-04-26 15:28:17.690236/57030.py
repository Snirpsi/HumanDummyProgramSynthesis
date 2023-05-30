#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or opens numbers. """    
    
    # Open a port on localhost
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    
    # Serve the webpage
    httpd.serve_forever()
    
