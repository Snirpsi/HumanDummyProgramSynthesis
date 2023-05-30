#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py filename=word