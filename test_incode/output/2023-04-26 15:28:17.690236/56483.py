#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or opens a list of words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
