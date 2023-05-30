#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and prints fruits. """    
    
    port = 8080
    
    # Open the webserver
    httpd = HTTPServer(('', port), FruitHandler)
    
    # Start the webserver
    httpd.serve_forever()
    
    # Stop the webserver
    httpd.server_close()
    
