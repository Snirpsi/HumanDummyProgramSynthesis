#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Get the list of numbers to iterate over
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create a webserver to iterate over the numbers
    server = HTTPServer(("", 80), MyHandler)
    
    # Start a webserver
    server.serve_forever()
