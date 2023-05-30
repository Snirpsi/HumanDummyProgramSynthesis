#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

<|/ file source=github ext=.py filename=server.py |>