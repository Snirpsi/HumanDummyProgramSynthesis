#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
