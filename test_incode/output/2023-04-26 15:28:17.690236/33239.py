#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or converts all ports. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()

<|/ file source=github |>