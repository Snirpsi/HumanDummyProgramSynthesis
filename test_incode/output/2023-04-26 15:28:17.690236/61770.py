#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()

<|/ file filename=word