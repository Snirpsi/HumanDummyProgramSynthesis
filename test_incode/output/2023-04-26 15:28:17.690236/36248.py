#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or stores words. """    
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
