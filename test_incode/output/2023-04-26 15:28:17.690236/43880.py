#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ["cat", "dog", "bird", "mouse"]
    
    server = HTTPServer(("localhost", 8080), Handler)
    
    print("Serving on localhost:8080")
    
    server.serve_forever()
