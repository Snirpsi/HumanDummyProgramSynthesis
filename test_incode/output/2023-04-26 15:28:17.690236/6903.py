#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and iterates over numbers. """    
    words = ['cat', 'dog', 'mouse', 'horse']
    numbers = [1, 2, 3, 4]
    
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()

<|/ file ext=.py filename=server.py |>