#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or removes a list of numbers. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
