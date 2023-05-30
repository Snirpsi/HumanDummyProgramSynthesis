#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    server = HTTPServer(("", 8080), MyHandler)
    
    print("Serving on port 8080...")
    
    server.serve_forever()
    
