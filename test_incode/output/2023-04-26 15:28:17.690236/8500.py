#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    server_address = ('localhost', 8080)
    
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
