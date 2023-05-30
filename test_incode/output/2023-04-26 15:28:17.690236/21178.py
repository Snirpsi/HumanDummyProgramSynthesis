#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or iterates over a port. """    
    port = 8080
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
