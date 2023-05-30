#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and opens words. """    
    
    # Open the port and enumerate its contents
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
