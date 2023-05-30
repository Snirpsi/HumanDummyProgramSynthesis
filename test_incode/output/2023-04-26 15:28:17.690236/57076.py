#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or prints a list of words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    
