#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and prints user input. """    
    
    numbers = [int(i) for i in input().split()]
    
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

<|/ file filename=server.py ext=.py |>